# code2prompt

> 코드베이스에서 AI용 프롬프트를 생성 (LLM을 위해 코드를 추출, 필터링, 포맷팅).
> 더 많은 정보: <https://code2prompt.dev/docs/how_to/filter_files/>.

- 현재 프로젝트에 대한 프롬프트를 생성하고 클립보드에 복사 (기본 동작):

`code2prompt {{경로/대상/프로젝트}}`

- 특정 파일만 포함하고 특정 디렉토리는 제외:

`code2prompt {{경로/대상/프로젝트}} {{[-i|--include]}} "{{**/*.rs}}" {{[-e|--exclude]}} "{{tests/**}}"`

- 클립보드 대신 파일에 프롬프트를 저장:

`code2prompt {{경로/대상/프로젝트}} {{[-O|--output-file]}} {{프롬프트.txt}}`

- 구조화된 JSON 형식으로 출력:

`code2prompt {{경로/대상/프로젝트}} {{[-F|--output-format]}} json`

- 프롬프트 생성 시 사용자 정의 Handlebars 템플릿을 사용:

`code2prompt {{경로/대상/프로젝트}} {{[-t|--template]}} {{템플릿.hbs}}`
