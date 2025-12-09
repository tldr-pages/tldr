# ssh-add

> `ssh-agent`에서 로드된 SSH 키를 관리.
> 키가 로드되도록 `ssh-agent`가 실행 중인지 확인하세요.
> 더 많은 정보: <https://man.openbsd.org/ssh-add>.

- 기본 SSH 키를 `~/.ssh`에서 ssh-agent로 추가:

`ssh-add`

- 특정 키를 ssh-agent로 추가:

`ssh-add {{경로/대상/개인_키}}`

- 현재 로드된 키의 지문 나열:

`ssh-add -l`

- ssh-agent에서 키 삭제:

`ssh-add -d {{경로/대상/개인_키}}`

- 현재 로드된 모든 키를 ssh-agent에서 삭제:

`ssh-add -D`

- 키를 ssh-agent와 키체인에 추가:

`ssh-add -K {{경로/대상/개인_키}}`
