# npm cache

> npm 패키지 캐시 관리.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-cache/>.

- 특정 패키지를 캐시에 추가:

`npm cache add {{패키지_이름}}`

- 키를 사용하여 특정 캐시 항목 삭제:

`npm cache clean {{키}}`

- 전체 npm 캐시 삭제:

`npm cache clean {{[-f|--force]}}`

- 캐시된 패키지 나열:

`npm cache ls`

- 특정 이름과 버전과 일치하는 캐시된 패키지 나열:

`npm cache ls {{이름}}@{{버전}}`

- npm 캐시의 무결성 확인:

`npm cache verify`

- npx 캐시의 모든 항목 나열:

`npm cache npx ls`
