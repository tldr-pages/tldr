# ssh-agent

> SSH 에이전트 프로세스 생성.
> SSH 에이전트는 SSH 키를 메모리에 복호화된 상태로 유지하며, 제거되거나 프로세스가 종료될 때까지 유지됩니다.
> 같이 보기: `ssh-add` (SSH 에이전트에 의해 관리되는 키 추가 및 관리).
> 더 많은 정보: <https://man.openbsd.org/ssh-agent>.

- 현재 셸에 대한 SSH 에이전트 시작:

`eval $(ssh-agent)`

- 현재 실행 중인 에이전트 종료:

`ssh-agent -k`
