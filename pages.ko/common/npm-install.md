# npm install

> Node 패키지 설치.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-install>.

- `package.json`에 나열된 의존성 설치:

`npm install`

- 특정 버전의 패키지를 다운로드하고 `package.json`의 의존성 목록에 추가:

`npm install {{패키지_이름}}@{{버전}}`

- 최신 버전의 패키지를 다운로드하고 `package.json`의 개발 의존성 목록에 추가:

`npm install {{패키지_이름}} {{[-D|--save-dev]}}`

- 최신 버전의 패키지를 다운로드하고 전역으로 설치:

`npm install {{[-g|--global]}} {{패키지_이름}}`
