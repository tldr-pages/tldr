# aider

> 원하는 LLM과 페어 프로그래밍을 진행.
> 더 많은 정보: <https://github.com/Aider-AI/aider>.

- 새 프로젝트를 시작하거나 기존 코드베이스에서 작업:

`aider --model {{모델_이름}} --api-key {{당신의_api_키}}`

- 특정 파일에 새로운 기능이나 테스트 케이스를 추가:

`aider {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 버그를 설명하고 `aider`가 이를 수정하도록 함:

`aider {{경로/대상/파일}} --describe "{{버그_설명}}"`

- 특정 파일의 코드를 리팩터링:

`aider {{경로/대상/파일}} --refactor`

- 문서 업데이트:

`aider {{경로/대상/파일}} --update-docs`

- 도움말 표시:

`aider --help`
