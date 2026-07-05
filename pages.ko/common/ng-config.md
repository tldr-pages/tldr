# ng config

> JSON 경로 표기법(camelCase)을 사용하여 Angular 워크스페이스 또는 프로젝트 설정(빌드 옵션 등) 편집.
> 더 많은 정보: <https://angular.dev/cli/config>.

- 모든 설정 값 표시:

`ng config`

- 특정 설정 값 조회:

`ng config projects.{{프로젝트_이름}}.prefix`

- 특정 설정 값 변경:

`ng config projects.{{프로젝트_이름}}.prefix {{값}}`

- Angular CLI 분석 기능 전역 비활성화:

`ng config cli.analytics disabled {{[-g|--global]}}`

- 전역 설정 값 변경 (주의: 모든 Angular 프로젝트에 영향을 줄 수 있음):

`ng config projects.{{프로젝트_이름}}.prefix {{값}} {{[-g|--global]}}`
