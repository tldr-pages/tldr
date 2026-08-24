# openclaw

> 개인 기기에서 실행되는 개인 AI 어시스턴트.
> `onboard`, `agent`, `doctor`와 같은 일부 하위 명령어는 별도의 사용법 문서를 가짐.
> 관련 항목: `zeroclaw`.
> 더 많은 정보: <https://docs.openclaw.ai/cli>.

- 게이트웨이 및 채널 설정을 위한 온보딩 실행:

`openclaw onboard --install-daemon`

- 게이트웨이 서버 시작:

`openclaw gateway --allow-unconfigured --port {{18789}} --verbose`

- 연락처에 메시지 전송:

`openclaw message send {{[-t|--target]}} {{+1234567890}} {{[-m|--message]}} "{{Hello}}"`

- 단일 메시지로 AI 어시스턴트와 대화:

`openclaw agent {{[-m|--message]}} "{{Ship checklist}}"`

- 대화형 채팅 모드 시작:

`openclaw agent`

- 시스템 상태 점검 및 진단 실행:

`openclaw doctor`

- OpenClaw 최신 버전으로 업데이트:

`openclaw update`

- 설정된 채널 목록 출력:

`openclaw channels list`
