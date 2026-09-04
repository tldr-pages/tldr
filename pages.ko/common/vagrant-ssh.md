# vagrant ssh

> 실행 중인 Vagrant machine애 SSH로 접속.
> 관련 항목: `vagrant`.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/ssh>.

- 현재 디렉터리에서 실행 중인 machine에 SSH로 접속:

`vagrant ssh`

- 이름 또는 ID를 지정하여 실행 중임 machine에 접속:

`vagrant ssh {{이름|id}}`

- SSH 명령을 실행하고 종료:

`vagrant ssh {{[-c|--command]}} {{ssh_명령}}`

- 사용자가 인증은 직접 수행하며, 자동 인증을 사용하지 않고 SSH로 접속:

`vagrant ssh {{[-p|--plain]}}`
