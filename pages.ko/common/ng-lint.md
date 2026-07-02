# ng lint

> 설정된 린터를 사용하여 Angular 프로젝트의 코드 스타일 및 오류 검사.
> 참고: 린트 기능은 먼저 `ng add`를 통해 설정해야 함.
> 더 많은 정보: <https://angular.dev/cli/lint>.

- 워크스페이스의 모든 프로젝트 린트 검사:

`ng lint`

- 특정 프로젝트 린트 검사:

`ng lint {{프로젝트_이름}}`

- 린트 오류 자동 수정:

`ng lint {{프로젝트_이름}} --fix`

- 린트 오류가 있어도 성공(exit code 0)으로 처리:

`ng lint {{프로젝트_이름}} --force`

- 특정 출력 형식 사용:

`ng lint {{프로젝트_이름}} --format {{stylish|json|...}}`
