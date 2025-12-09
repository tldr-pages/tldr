# npm cache

> npm 패키지 캐시 관리.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-cache>.

- 특정 패키지를 캐시에 추가:

`npm cache add {{패키지_이름}}`

- 특정 패키지를 캐시에서 제거:

`npm cache remove {{패키지_이름}}`

- 키를 사용하여 특정 캐시 항목 삭제:

`npm cache clean {{키}}`

- 전체 npm 캐시 삭제:

`npm cache clean --force`

- npm 캐시의 내용 나열:

`npm cache ls`

- npm 캐시의 무결성 확인:

`npm cache verify`

- npm 캐시 위치 및 구성 정보 표시:

`npm cache dir`

- 캐시 경로 변경:

`npm config set cache {{경로/대상/폴더}}`
