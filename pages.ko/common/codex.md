# codex

> OpenAI로 구동되는 터미널용 자연어 코드 어시스턴트.
> 요청을 수행하기 위해 현재 디렉터리의 파일을 읽고 수정.
> 더 많은 정보: <https://github.com/openai/codex>.

- 현재 디렉터리에서 대화형 Codex 세션을 시작:

`codex`

- 프롬프트를 사용해 단일 Codex 명령을 실행:

`codex "{{프롬프트}}"`

- 프롬프트를 전체 자동 모드로 실행:

`codex --full-auto "{{프롬프트}}"`

- 특정 모델을 사용:

`codex {{[-m|--model]}} {{모델_이름}} "{{프롬프트}}"`

- 로컬 오픈소스 모델 제공자를 사용:

`codex --oss --local-provider {{lmstudio|ollama}} "{{프롬프트}}"`

- [대화형] 현재 세션의 리소스 사용량을 표시:

`/cost`

- 도움말 표시:

`codex {{[-h|--help]}}`
