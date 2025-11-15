# standard

> JavaScript 코드의 린트 및 수정을 위한 JavaScript Standard Style 도구.
> 더 많은 정보: <https://standardjs.com>.

- 현재 디렉토리의 모든 JavaScript 소스 파일을 린트:

`standard`

- 특정 JavaScript 파일(들)을 린트:

`standard {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 린트 시 자동 수정 적용:

`standard --fix`

- 사용 가능한 전역 변수 선언:

`standard --global {{변수}}`

- 린트 시 사용자 지정 ESLint 플러그인 사용:

`standard --plugin {{플러그인}}`

- 린트 시 사용자 지정 JS 파서 사용:

`standard --parser {{파서}}`

- 린트 시 사용자 지정 ESLint 환경 사용:

`standard --env {{환경}}`
