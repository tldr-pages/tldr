# openclaw agent

> OpenClaw AI 어시스턴트와 대화하는 명령어.
> 더 많은 정보: <https://docs.openclaw.ai/cli/agent>.

- 단일 메시지로 어시스턴트와 대화:

`openclaw agent {{[-m|--message]}} "{{Hello, what is the weather?}}"`

- 대화형 채팅 모드 시작:

`openclaw agent`

- 사고(thinking) 수준을 설정해 메시지 전송:

`openclaw agent {{[-m|--message]}} "{{Analyze this}}" --thinking {{off|minimal|low|medium|high}}`

- 도움말 표시:

`openclaw agent {{[-h|--help]}}`
