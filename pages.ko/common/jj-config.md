# jj config

> 설정 옵션을 관리.
> `edit`, `get`, `list`, `path`, `set`, `unset` 등의 일부 하위 명령은 각각 별도의 사용 문서를 가짐.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-config>.

- 사용자 수준 설정 파일을 편집기로 열기:

`jj config {{[e|edit]}} --user`

- 설정 옵션 값 조회:

`jj config {{[g|get]}} {{이름}}`

- 모든 설정 변수와 값 목록 표시:

`jj config {{[l|list]}}`

- 사용자 수준 설정 파일 경로 출력:

`jj config {{[p|path]}} --user`

- 사용자 수준 설정 파일에 설정 옵션 추가 또는 변경:

`jj config {{[s|set]}} --user {{이름}} {{값}}`

- 사용자 수준 설정 파일에서 설정 옵션 제거:

`jj config {{[u|unset]}} --user {{이름}}`
