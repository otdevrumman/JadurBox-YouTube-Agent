# Cross-agent handoff

All agent operations are **logical orchestration** unless the current host provides verified direct subagent execution.

1. Main Agent creates project task brief and status.
2. Growth Agent produces evidence-backed topic strategy; Growth QA reviews figures and claims; creator selects priority.
3. Research Agent creates fact brief + claim ledger; Research QA independently checks critical sources and returns verdict.
4. Script Agent creates numbered draft from reviewed research.
5. Script QA returns PASS / REVISE / FACT-CHECK INCOMPLETE with evidence.
6. Creator approves the script explicitly.
7. Asset Agent sources visuals with provenance and licenses; Asset QA independently reviews candidate media; creator decides whether assets may be used.
8. Video Agent uses approved media and verified timing, prepares **editable preview**.
9. Video QA reviews preview and reports PASS / REVISE / NOT VERIFIED.
10. Creator authorizes rendering explicitly (e.g. `render koro`).
11. Render validation by Video QA; creator authorizes publication separately.

## Handoff template

```yaml
project_id: ""
topic: ""
phase: ""
agent_from: ""
agent_to: ""
script_version: ""
source_paths: []
assets_verified: []
status: "READY_FOR_REVIEW"
qa_evidence: []
issues: []
creator_approval: false
next_action: ""
```
