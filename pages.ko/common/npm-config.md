# npm config

> `npm` 설정을 관리하는 명령어.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-config/>.

- 모든 설정 값 출력:

`npm {{[c|config]}} list`

- 모든 설정을 `JSON` 형식으로 출력:

`npm {{[c|config]}} list --json`

- 특정 설정 값 조회:

`npm {{[c|config]}} get {{키}}`

- 설정 키에 값을 지정:

`npm {{[c|config]}} set {{키}} {{value}}`

- 설정 키 삭제:

`npm {{[c|config]}} delete {{키}}`

- 기본 편집기로 전역 npm 설정 파일 수정:

`npm {{[c|config]}} edit`

- 잘못된 설정 항목 자동 수정 시도:

`npm {{[c|config]}} fix`
