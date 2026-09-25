# jj config get

> 지정한 설정 옵션의 값을 조회.
> `jj config list`와 달리, 스크립트에서 사용할 수 있도록 추가 서식 없이 값을 출력.
> 관련 항목: `jj config list`.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-config-get>.

- 설정 옵션 값 조회:

`jj config {{[g|get]}} {{이름}}`

- 설정된 사용자 이름 조회:

`jj config {{[g|get]}} user.name`

- 설정된 사용자 이메일 조회:

`jj config {{[g|get]}} user.email`

- log 명령의 기본 revset 조회:

`jj config {{[g|get]}} revsets.log`
