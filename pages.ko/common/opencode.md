# opencode

> AI 코딩 에이전트.
> `auth`, `models`, `web`와 같은 일부 하위명령어는 별도의 사용법 문서를 가짐
> 더 많은 정보: <https://opencode.ai/docs/cli/>.

- 대화형 TUI 시작:

`opencode`

- 가장 최근 세션 이어서 실행:

`opencode {{[-c|--continue]}}`

- 프롬프트를 직접 전달하여 비대화형으로 실행:

`opencode run "{{메시지}}"`

- 특정 모델과 에이전트를 지정하여 실행:

`opencode run {{[-m|--model]}} {{제공자}}/{{모델}} --agent {{에이전트_이름}} "{{메시지}}"`

- 설정된 제공자에서 사용 가능한 모델 목록 출력:

`opencode models`

- 제공자 인증 및 로그인 관리:

`opencode auth login`

- API 접근을 위한 헤드리스 서버 실행:

`opencode serve {{[-h|--hostname]}} {{호스트명}} {{[-p|--port]}} {{포트}}`

- 사용자 정의 설정으로 새로운 에이전트 생성:

`opencode agent create`
