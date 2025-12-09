# npm

> JavaScript 및 Node.js 패키지 관리자.
> Node.js 프로젝트 및 모듈 의존성을 관리합니다.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm>.

- 기본값으로 `package.json` 파일 생성 (`--yes`를 생략하면 대화식으로 진행):

`npm init {{[-y|--yes]}}`

- package.json에 의존성으로 나열된 모든 패키지를 다운로드:

`npm install`

- 특정 버전의 패키지를 다운로드하고 `package.json`의 의존성 목록에 추가:

`npm install {{패키지_이름}}@{{버전}}`

- 최신 버전의 패키지를 다운로드하고 `package.json`의 개발 의존성 목록에 추가:

`npm install {{패키지_이름}} {{[-D|--save-dev]}}`

- 최신 버전의 패키지를 다운로드하여 전역적으로 설치:

`npm install {{[-g|--global]}} {{패키지_이름}}`

- 패키지를 제거하고 `package.json`의 의존성 목록에서 제거:

`npm uninstall {{패키지_이름}}`

- 로컬에 설치된 모든 의존성 나열:

`npm list`

- 전역적으로 설치된 최상위 패키지 나열:

`npm list {{[-g|--global]}} --depth {{0}}`
