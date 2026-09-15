# poetry new

> 지정한 디렉터리의 새로운 Poetry 프로젝트 생성.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#new>.

- 새로운 프로젝트 생성 (기본값은 `src` 레이아웃):

`poetry new {{경로/대상/디렉터리}}`

- 설정 정보를 대화형으로 입력해 새로운 프로젝트 생성:

`poetry new {{경로/대상/디렉터리}} {{[-i|--interactive]}}`

- 지정한 패키지 이름으로 새로운 프로젝트 생성:

`poetry new {{경로/대상/디렉터리}} --name {{패키지_이름}}`

- flat 레이아웃으로 새로운 프로젝트 생성 (`src` 디렉터리 없이):

`poetry new {{경로/대상/디렉터리}} --flat`

- 지정한 작성자 정보로 새로운 프로젝트 생성:

`poetry new {{경로/대상/디렉터리}} --author "{{Name <email@example.com>}}"`

- 지정한 README 형식으로 새로운 프로젝트 생성:

`poetry new {{경로/대상/디렉터리}} --readme {{md|rst|txt|...}}`
