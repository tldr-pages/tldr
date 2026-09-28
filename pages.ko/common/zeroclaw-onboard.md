# zeroclaw onboard

> ZeroClaw의 워크스페이스와 설정을 초기화.
> 더 많은 정보: <https://github.com/zeroclaw-labs/zeroclaw#quick-start>.

- API 키 및 provider를 지정해 빠르게 설정:

`zeroclaw onboard --api-key {{api_키}} --provider {{openrouter}}`

- 전체 대화형 설정 마법사 실행:

`zeroclaw onboard --interactive`

- 채널과 허용 목록만 다시 설정 (빠른 복구 절차):

`zeroclaw onboard --channels-only`

- 지정한 메모리 백엔드를 사용하여 빠르게 설정:

`zeroclaw onboard --api-key {{api_키}} --provider {{openrouter}} --memory {{sqlite}}`

- 도움말 표시:

`zeroclaw onboard {{[-h|--help]}}`
