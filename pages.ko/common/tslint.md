# tslint

> TypeScript를 위한 플러그 가능한 린트 유틸리티.
> 더 많은 정보: <https://palantir.github.io/tslint>.

- TSLint 구성 생성:

`tslint --init`

- 주어진 파일 집합에 대해 린트 수행:

`tslint {{경로/대상/파일1.js 경로/대상/파일2.js ...}}`

- 린트 문제 수정:

`tslint --fix`

- 프로젝트 루트에 있는 설정 파일로 린트 수행:

`tslint --project {{경로/대상/프로젝트_루트}}`
