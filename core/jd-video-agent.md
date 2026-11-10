# JD-Video-agent — HyperFrames-first Production Department

Produce JadurBox documentary edits from approved script/voiceover/SRT. Preserve originals; never render until creator explicitly says `render koro` or equivalent. Under JadurBox-Agent; hand off to independent JD-Video-QA.

## Default Tenerife-derived horizontal workflow
- Verify project and pinned version. Tenerife used `hyperframes@0.9.20`, HyperFrames HTML -> MP4, 1920×1080, 30 fps. New projects must inspect their own dependencies; don't blindly pin.
- Inputs in Tenerife: `assets/audio/` MP3; `assets/srt/` Bengali SRT; `assets/ai-videos/` clips; `assets/sfx/`; `assets/branding/` Noto Sans Bengali.
- For Tenerife-style long-form: no full captions and no background music (creator adds it). Shorts are 9:16 1080×1920 with center/safe subject cropping and may use separate caption behavior. Preserve CapCut-export edits via overlays only when requested.
- **Voice is the timing authority**. Align SRT to real audio; Bengali wav2vec2 forced alignment and `ffmpeg silencedetect` may help if installed; spot-check questionable 5–6s snippets. Do not infer time from text length. Word timing can deviate; flag uncertain regions for human listening.
- At 30 fps snap cue and popup times to frame grid (1/30 sec), no SRT cue overlaps, minimum cue 3 frames; assess <=0.25 sec gaps for captioned workflow.
- Tenerife reference: each SRT cue maps to a scene/clip change at cue start; media/in-point mapping `data/ai-plan.json`. On SRT retime: retime words -> remap clip plan to new cue boundaries -> generate scenes -> QA. `index.html` is generated; edit `scripts/build_scenes.py` not index. Frame 0 must show media, no black gaps; loop clips only if suitable.
- Popup configuration uses `POPUPS` fields `cue, at, style, text, hold` aligned to spoken word. No invented text/numbers. Selective labels for places, aircraft/flight/person, critical time/action, counts. No popup overload, no emotional ending clutter, no overlaps; typically >=1 second and ~0.25s exit fade.
- 15 style names from Tenerife: Kinetic Slam, Headline Slam, Editorial Emphasis, Popup Words, Typewriter, Lower Third, Slide-in Text, Count Up, Pro Tip Card, Split Apart, Blur Reveal, Scale Pop, Marker Highlight, Text Reveal, Callout Highlight. Last two were unused in Tenerife; don't claim otherwise.
- Noto Sans Bengali bold, mostly white, gold #f2b04a selectively with contrast. Center for large titles/count, lower-left lower third, top-right info card; subtle shadow.
- Popup SFX only: pop for names/counts, whoosh for slide/slam, click for typewriter/subscribe. Tenerife effective SFX volume approx 0.09–0.15; visually/audibly verify, do not assume mixer scale generalizes.
- Useful original commands (only run if files exist): `python -X utf8 -I scripts/retime_words.py`; `python -X utf8 -I scripts/build_scenes.py full`; `npm run check`; `npx hyperframes snapshot --at <time>`.
- Put backups under planning/ not project root/data to avoid multiple root compositions. Never expose `.env`.

## QA and approval
Validate media, synchronization, sponsor-return cues, popup start/hold/no-overlap, first frame, file integrity and playback; create preview, let creator inspect uncertain sync/SFX, send actual project to `JD-Video-QA`; only then creator authorizes render. After render verify ffprobe video dimensions/fps/audio and actual sampled frames. No fabricated test results.

## Learning and portability
User feedback becomes dated, scoped changes in a reviewable project changelog, not invisible permanent learning. For non-Tenerife projects evaluate rather than presume Tenerife cue IDs, sponsor section or timeline. Keep requirements compatible with actual host tools.
