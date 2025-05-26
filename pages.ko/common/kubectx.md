# kubectx

> `kubectl` 컨텍스트를 관리하고 전환하는 도구.
> 더 많은 정보: <https://manned.org/kubectx>.

- 컨텍스트 나열:

`kubectx`

- 지정된 이름의 컨텍스트로 전환:

`kubectx {{이름}}`

- 이전 컨텍스트로 전환:

`kubectx -`

- 지정된 이름의 컨텍스트 이름 변경:

`kubectx {{별칭}}={{이름}}`

- 현재 사용 중인 컨텍스트 표시:

`kubectx -c`

- 지정된 이름의 컨텍스트 삭제:

`kubectx -d {{이름}}`
