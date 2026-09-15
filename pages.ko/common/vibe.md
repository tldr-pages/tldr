# vibe

> 터미널에서 사용하는 MistralAI 기반 자연어 코드 어시스턴트.
> 현재 디렉터리의 파일을 읽고 수정하여 요청을 수행.
> 더 많은 정보: <https://github.com/mistralai/mistral-vibe#usage>.

- 현재 디렉터리에서 대화형 Mistral Vibe 세션 시작:

`vibe`

- 현재 디렉터리의 가장 최근 Vibe 세션 이어서 실행:

`vibe {{[-c|--continue]}}`

- API 키 설정을 위한 대화형 Vibe 세션을 시작한 후 종료:

`vibe --setup`

- 파일 수정과 명령 실행을 자동 승인해 단일 Vibe 프롬프트 실행:

`vibe {{[-p|--prompt]}} "{{당신의_프롬프트}}"`

- 지정한 출력 형식으로 단일 Vibe 프롬프트 실행:

`vibe --output {{json|text|streaming}} {{[-p|--prompt]}} "{{당신의_프롬프트}}"`
