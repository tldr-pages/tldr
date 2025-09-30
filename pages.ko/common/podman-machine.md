# podman machine

> Podman을 실행하는 가상 머신을 생성하고 관리.
> Podman 버전 4 이상에 포함되어 있습니다.
> 더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

- 기존 머신 나열:

`podman machine ls`

- 기본 머신 생성:

`podman machine init`

- 특정 이름의 새 머신 생성:

`podman machine init {{이름}}`

- 다른 리소스로 새 머신 생성:

`podman machine init --cpus={{4}} --memory={{4096}} --disk-size={{50}}`

- 머신 시작 또는 중지:

`podman machine {{start|stop}} {{이름}}`

- SSH를 통해 실행 중인 머신에 연결:

`podman machine ssh {{이름}}`

- 머신 정보 검사:

`podman machine inspect {{이름}}`
