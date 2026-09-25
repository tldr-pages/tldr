# ng add

> 현재 Angular 워크스페이스 프로젝트에 패키지를 추가하고 설정.
> 더 많은 정보: <https://angular.dev/cli/add>.

- 현재 프로젝트에 패키지 추가:

`ng add {{패키지}}`

- 여러 패키지 추가:

`ng add {{패키지1 패키지2 ...}}`

- 특정 버전의 패키지 추가:

`ng add {{패키지}}@{{버전}}`

- 확인 프롬프트 건너뛰기:

`ng add {{패키지}} --skip-confirmation`

- 대화형 프롬프트 비활성화:

`ng add {{패키지}} --interactive false`

- 내부 작업에 대한 상세 로그 출력:

`ng add {{패키지}} --verbose`

- 실제 변경 없이 실행 결과만 확인:

`ng add {{패키지}} {{[-d|--dry-run]}}`
