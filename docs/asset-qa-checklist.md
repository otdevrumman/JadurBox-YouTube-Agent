# JD-Asset-QA check list

## Required asset data
- Asset ID / project ID / scene and SRT cue / format (photo, video, AI)
- Actual asset landing page and provider/creator
- Copyright/licensing evidence URL + terms access date, attribution text, allowed usage and restrictions
- Provenance category (`AUTHENTIC_ARCHIVAL`, `CONTEMPORARY_STOCK`, `HISTORICAL_RECONSTRUCTION`, `AI_GENERATED`)
- Actual filename (if provided), sha256 (if available), dimensions, duration/fps for video, desired crop
- Evidence for historical claims (incident, year, place, visual identity), reconstruction disclaimer when needed
- Any required permission/release and risk owner

## Critical red flags
1. Broken/invented URL or asset page doesn't match claimed asset
2. License unverified, misquoted, attribution missing or commercial/redistribution restriction ignored
3. AI-generated or generic stock footage described as real archival image
4. Incorrect aircraft, historic date, country, tools, map or casualty count
5. Watermarked/unlicensed or corrupted media, wrong ratio or cropped primary subject
6. Any exposed API key or credentials

## Verification evidence format
`asset_id | claim | observed evidence link/file | verified_date | status | reason | fix | owner`
Do not claim to have personally watched/listened to media when only metadata was available. Use qualitative visual inspection only if actual frames are available. Do not assume API results grant a license.
