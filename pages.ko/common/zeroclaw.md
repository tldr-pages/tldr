# zeroclaw

> 빠르게 가볍게 동작하는 완전 자율형 AI 어시스턴트 인프라.
> `onboard`, `models`, `service` 등의 일부 하위 명령은 각각 별도의 사용 문서를 제공.
> 관련 항목: `openclaw`.
> 더 많은 정보: <https://github.com/zeroclaw-labs/zeroclaw#quick-start>.

- 워크스페이스와 설정 초기화 (빠른 설정):

`zeroclaw onboard --api-key {{api_키}} --provider {{openrouter|anthropic|openai|...}}`

- 전체 대화형 온보딩 마법사 실행:

`zeroclaw onboard --interactive`

- AI 에이전트에 단일 메시지 전송:

`zeroclaw agent {{[-m|--message]}} "{{Hello, ZeroClaw!}}"`

- 대화형 채팅 모드 시작:

`zeroclaw agent`

- 게이트웨이 서버 시작 (기본값: 127.0.0.1:8080):

`zeroclaw gateway`

- 전체 자율 런타임 시작 (게이트웨이 + 채널 + 하트비트):

`zeroclaw daemon`

- 시스템 상태 확인:

`zeroclaw status`

- 진단 실행:

`zeroclaw doctor`
