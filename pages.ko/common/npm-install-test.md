# npm install-test

> `npm install` 후 `npm test`를 실행하는 것과 동일한 명령어.
> 참고: `it`은 `install-test`의 단축 명령으로 사용할 수 있음.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-install-test/>.

- 모든 의존성 설치 후 테스트 실행:

`npm {{[it|install-test]}}`

- 특정 패키지 설치 후 테스트 실행:

`npm {{[it|install-test]}} {{패키지_이름}}`

- 패키지를 의존성으로 저장한 후 테스트 실행:

`npm {{[it|install-test]}} {{패키지_이름}} {{[-S|--save]}}`

- 전역으로 의존성 설치 후 테스트 실행:

`npm {{[it|install-test]}} {{[-g|--global]}}`
