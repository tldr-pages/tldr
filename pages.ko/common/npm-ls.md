# npm ls

> 설치된 패키지를 `stdout`로 출력.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-ls/>.

- 현재 프로젝트의 직접 의존성 버전을 `stdout`으로 출력:

`npm {{[ls|list]}}`

- peer 의존성을 포함한 모든 패키지 출력:

`npm {{[ls|list]}} {{[-a|--all]}}`

- 전역으로 설치된 모든 패키지 출력:

`npm {{[ls|list]}} {{[-g|--global]}}`

- 확장 정보와 함께 의존성 출력:

`npm {{[ls|list]}} {{[-l|--long]}}`

- 파싱 가능한 형식으로 출력:

`npm {{[ls|list]}} {{[-p|--parseable]}}`

- JSON 형식으로 출력:

`npm {{[ls|list]}} --json`
