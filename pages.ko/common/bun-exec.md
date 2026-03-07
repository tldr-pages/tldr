# bun exec

> Bun 런타임을 사용해 셸 명령어나 스크립트 파일을 실행
> 참고: 셸에서 실행할 때는, 따옴표를 이스케이프(escape)해야 합니다.
> 더 많은 정보: <https://bun.com/docs/runtime/shell>.

- 단일 명령어 실행:

`bun exec "echo hello"`

- 플래그를 가진 명령어를 실행:

`bun exec "ls -la"`

- 따옴표를 포함한 명령어를 실행:

`bun exec "echo \"hello friends\""`

- 조합된 셸 명령어를 실행:

`bun exec "mkdir test && cd test"`

- 스크립트 파일을 실행:

`bun exec {{경로/대상/스크립트}}`
