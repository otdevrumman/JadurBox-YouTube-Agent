#!/usr/bin/env python3
"""Generate portable Claude/Gemini/Codex agent adapters from canonical core files.

Usage: python scripts/sync_agents.py [--check]
No third-party dependencies. Never writes outside the current repository.
"""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
NAMES=['jadurbox-main','jd-script-agent','jd-script-qa','jd-video-agent','jd-video-qa','jd-asset-agent','jd-asset-qa','jd-research-agent','jd-research-qa','jd-growth-agent','jd-growth-qa']
DESCS={
 'jadurbox-main':'Direct the JadurBox production and growth team with human approval gates.',
 'jd-script-agent':'Write and revise verified Bangladeshi Bengali documentary scripts using the JadurBox 13-step structure.',
 'jd-script-qa':'Independently fact-check and review JadurBox Bengali documentary scripts before creator approval.',
 'jd-video-agent':'Edit JadurBox HyperFrames documentary projects with voiceover-SRT timing, popups, SFX, and preview before render.',
 'jd-video-qa':'Independently inspect JadurBox video preview and render quality, framing, voice-SRT timing, SFX and popups.',
 'jd-asset-agent':'Source JadurBox documentary photo/video/archival assets with exact provenance and optional secure local search APIs.',
 'jd-asset-qa':'Independently review JadurBox asset source links, licenses, media integrity, archival authenticity and AI disclosures.',
 'jd-research-agent':'Research JadurBox documentary topics using primary sources, verified chronology, and evidence ledgers.',
 'jd-research-qa':'Independently verify JadurBox research sources, casualty counts, historical facts and disputed claims.',
 'jd-growth-agent':'Analyze JadurBox channel analytics, content opportunities and SEO using dated verified sources.',
 'jd-growth-qa':'Independently check JadurBox growth metrics, comparisons, recommendations and SEO integrity.'
}

def safe_yaml(v): return "'"+v.replace("'","''")+"'"

def make():
 common=(ROOT/'core/COMMON.md').read_text(encoding='utf-8').strip()
 result={}
 for name in NAMES:
  role=(ROOT/f'core/{name}.md').read_text(encoding='utf-8').strip()
  instructions=common+'\n\n'+role+'\n'
  desc=DESCS[name]
  claude=f'---\nname: {name}\ndescription: {safe_yaml(desc)}\n---\n\n'+instructions
  gemini=f'---\nname: {name}\ndescription: {safe_yaml(desc)}\nkind: local\n---\n\n'+instructions
  codex=f'---\nname: {name}\ndescription: {safe_yaml(desc)}\n---\n\n'+instructions
  result[f'.claude/agents/{name}.md']=claude
  result[f'.gemini/agents/{name}.md']=gemini
  result[f'.agents/skills/{name}/SKILL.md']=codex
 return result

def main():
 check='--check' in sys.argv
 stale=[]
 for path,content in make().items():
  target=ROOT/path
  if not target.exists() or target.read_text(encoding='utf-8')!=content:
   stale.append(path)
   if not check:
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(content,encoding='utf-8')
 if stale and check:
  print('OUT OF SYNC: '+', '.join(stale));return 1
 print(('Verified' if check else 'Generated')+f' {len(NAMES)*3} agent adapters.');return 0
if __name__=='__main__':raise SystemExit(main())
