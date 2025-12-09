# nx

> `nx` 작업 공간 관리 도구.
> 더 많은 정보: <https://nx.dev/l/r/getting-started/nx-cli>.

- 특정 프로젝트 빌드:

`nx build {{프로젝트}}`

- 특정 프로젝트 테스트:

`nx test {{프로젝트}}`

- 특정 프로젝트에서 대상 실행:

`nx run {{프로젝트}}:{{대상}}`

- 여러 프로젝트에서 대상 실행:

`nx run-many --target {{대상}} --projects {{프로젝트1}},{{프로젝트2}}`

- 작업 공간의 모든 프로젝트에서 대상 실행:

`nx run-many --target {{대상}} --all`

- 변경된 프로젝트에서만 대상 실행:

`nx affected --target {{대상}}`
