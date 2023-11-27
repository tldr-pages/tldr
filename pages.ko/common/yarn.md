# yarn

> JavaScript 및 Node.js 패키지 대체 관리자.
> 더 많은 정보: <https://yarnpkg.com>.

- 전역적으로 모듈 설치:

`yarn global add {{모듈_이름}}`

- `package.json` 파일에 참조된 모든 의존성을 설치 ( `install`은 선택 사항입니다):

`yarn install`

- 모듈을 설치하고 `package.json` 파일에 대한 의존성으로 저장 (개발 전용 의존성으로 추가하려면 `--dev` 추가):

`yarn add {{모듈_이름}}@{{버전}}`

- 모듈을 제거하고 `package.json` 파일에서 제거:

`yarn remove {{모듈_이름}}`

- 대화형으로 `package.json` 파일 생성:

`yarn init`

- 모듈이 의존성인지 확인하고, 해당 모듈에 의존성이 있는 다른 모듈을 나열:

`yarn why {{모듈_이름}}`
