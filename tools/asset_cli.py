#!/usr/bin/env python3
"""JadurBox local optional API client. Python 3.10+ stdlib only.

Examples:
  python tools/asset_cli.py pixabay-photos 'airport runway' --limit 5
  python tools/asset_cli.py pixabay-videos 'airplane' --limit 5
  python tools/asset_cli.py unsplash 'ancient egypt' --limit 5
  python tools/asset_cli.py pollinations 'cinematic archaeological site' --output outputs/site.jpg --confirm-spend

This tool intentionally does not print keys or raw API URLs containing a key.
Search only writes a metadata JSON. Always review item licenses and attribution.
"""
import argparse
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent

def load_env():
    """Minimal .env loader; never print values and never override exported variables."""
    path = ROOT / '.env'
    if not path.exists():
        return
    for raw in path.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        name, value = line.split('=', 1)
        name = name.strip()
        value = value.strip().strip('"').strip("'")
        if name in ('PIXABAY_API_KEY','UNSPLASH_API_KEY','POLLINATIONS_API_KEY','Unsplash_API_KEY','Pollinations_API_KEY'):
            os.environ.setdefault(name, value)

def secret(name, *aliases):
    value = next((os.environ.get(n) for n in (name,*aliases) if os.environ.get(n)), None)
    if not value:
        raise RuntimeError(f"Missing {name}. Add it to the local .env (never GitHub).")
    return value

def request_bytes(url, headers=None, timeout=30):
    req = urllib.request.Request(url, headers={'User-Agent':'JadurBox-Asset-Agent/0.1',**(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        # Avoid leaking request URL (Pixabay query includes credentials).
        raise RuntimeError(f'Provider returned HTTP {exc.code}. Check the key, rate limit and provider documentation.') from None
    except urllib.error.URLError:
        raise RuntimeError('Network request failed. Check connectivity and firewall.') from None

def search_pixabay(query, video, limit):
    key=secret('PIXABAY_API_KEY')
    base='https://pixabay.com/api/videos/' if video else 'https://pixabay.com/api/'
    url=base+'?'+urllib.parse.urlencode({'key':key,'q':query,'per_page':max(3,min(200,limit)),'safesearch':'true'})
    raw=json.loads(request_bytes(url))
    found=[]
    for item in raw.get('hits',[])[:limit]:
        out={'provider':'Pixabay','type':'stock_video' if video else 'stock_photo','id':item.get('id'), 'page_url':item.get('pageURL'), 'creator':item.get('user'),'license_status':'REVIEW_REQUIRED','license_info':'https://pixabay.com/service/license-summary/'}
        if video:
            sizes=item.get('videos') or {}
            out['preview_url']=(sizes.get('medium') or sizes.get('small') or {}).get('url')
        else:
            out['preview_url']=item.get('webformatURL')
        found.append(out)
    return found

def search_unsplash(query, limit):
    key=secret('UNSPLASH_API_KEY','Unsplash_API_KEY')
    url='https://api.unsplash.com/search/photos?'+urllib.parse.urlencode({'query':query,'per_page':min(30,limit),'content_filter':'high'})
    raw=json.loads(request_bytes(url, headers={'Authorization':'Client-ID '+key,'Accept-Version':'v1'}))
    return [{'provider':'Unsplash','type':'stock_photo','id':x.get('id'),'page_url':(x.get('links') or {}).get('html'),'creator':(x.get('user') or {}).get('name'), 'creator_page':((x.get('user') or {}).get('links') or {}).get('html'), 'preview_url':(x.get('urls') or {}).get('small'), 'license_status':'REVIEW_REQUIRED','license_info':'https://unsplash.com/license','download_tracking_required':True} for x in raw.get('results',[])[:limit]]

def generate_pollinations(prompt,output,model):
    key=secret('POLLINATIONS_API_KEY','Pollinations_API_KEY')
    params={'model':model} if model else {}
    quoted=urllib.parse.quote(prompt,safe='')
    url='https://gen.pollinations.ai/image/'+quoted+(('?'+urllib.parse.urlencode(params)) if params else '')
    content=request_bytes(url,headers={'Authorization':'Bearer '+key},timeout=120)
    out=pathlib.Path(output)
    if out.exists():
        raise RuntimeError(f'Output file already exists: {out}; select another filename to avoid overwrite.')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_bytes(content)
    return {'provider':'Pollinations','type':'AI_GENERATED','output':str(out),'bytes':len(content),'model_requested':model or 'provider-default','auth':'environment-only','needs_historical_reconstruction_label':True}

def main():
    load_env()
    parser=argparse.ArgumentParser(description='Search documentary media; generate AI only with explicit confirmation.')
    parser.add_argument('mode',choices=['pixabay-photos','pixabay-videos','unsplash','pollinations'])
    parser.add_argument('query',help='English search query or generation prompt')
    parser.add_argument('--limit',type=int,default=10)
    parser.add_argument('--output',default='')
    parser.add_argument('--model',default='')
    parser.add_argument('--confirm-spend',action='store_true',help='Explicitly authorize potentially paid generation')
    a=parser.parse_args()
    try:
        if a.mode=='pollinations':
            if not a.confirm_spend or not a.output:
                raise RuntimeError('Image generation may incur charges. Use --confirm-spend and --output after approval.')
            result=generate_pollinations(a.query,a.output,a.model)
        else:
            if a.limit<1 or a.limit>30:
                raise RuntimeError('Search --limit must be between 1 and 30')
            result=search_unsplash(a.query,a.limit) if a.mode=='unsplash' else search_pixabay(a.query, a.mode=='pixabay-videos',a.limit)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except RuntimeError as exc:
        print('ERROR: '+str(exc),file=sys.stderr)
        sys.exit(1)

if __name__=='__main__':main()
