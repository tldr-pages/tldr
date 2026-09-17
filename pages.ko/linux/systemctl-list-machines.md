# systemctl list-machines

> 호스트와 현재 실행 중인 모든 로컬 가상 머신 또는 컨테이너를 상태와 함께 나열.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-machines%20PATTERN%E2%80%A6>.

- 모든 머신 (호스트 및 실행 중인 컨테이너 및 VM) 출력:

`systemctl list-machines`

- 특정 머신 출력:

`systemctl list-machines {{머신}}`

- 여러 머신 출력:

`systemctl list-machines {{머신_1 머신_2 ...}}`

- 와일드카드 패턴(즉, `shell-globbing`)으로 머신 필터링:

`systemctl list-machines {{패턴}}`
