# jj config set

> 설정 옵션에 지정한 값을 설정.
> 값은 TOML 표현식으로 지정.
> 관련 항목: `jj config unset`.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-config-set>.

- 사용자 수준 설정 파일에 사용자 이름 설정:

`jj config {{[s|set]}} --user user.name "{{이름}}"`

- 사용자 수준 설정 파일에 사용자 이메일 설정:

`jj config {{[s|set]}} --user user.email "{{이메일}}"`

- 저장소 수준 설정 파일에 설정 옵션 설정:

`jj config {{[s|set]}} --repo {{이름}} {{값}}`

- 작업 공간 수준 설정 파일에 설정 옵션 설정:

`jj config {{[s|set]}} --workspace {{이름}} {{값}}`

- boolean 설정 옵션 설정:

`jj config {{[s|set]}} --user {{이름}} {{true|false}}`
