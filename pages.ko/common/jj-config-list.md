# jj config list

> 설정 파일에 정의된 설정 변수와 값을 표시.
> 관련 항목: `jj config get`.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-config-list>.

- 모든 설정 변수와 값 목록 표시:

`jj config {{[l|list]}}`

- 지정한 설정 옵션 표시:

`jj config {{[l|list]}} {{이름}}`

- 사용자 수준 설정 변수 목록 표시:

`jj config {{[l|list]}} --user`

- 저장소 수준 설정 변수 목록 표시:

`jj config {{[l|list]}} --repo`

- 기본 내장값을 포함하여 설정 변수 목록 표시:

`jj config {{[l|list]}} --include-defaults`

- 재정의된 값을 포함하여 설정 변수 목록 표시:

`jj config {{[l|list]}} --include-overridden`

- 사용자 지정 템플릿으로 설정 변수 목록 표시:

`jj config {{[l|list]}} {{[-T|--template]}} {{템플릿}}`
