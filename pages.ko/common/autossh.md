# autossh

> SSH 연결을 실행, 모니터링 및 재시작. 
> 포트 포워딩 터널이 유지되도록 자동으로 재연결. SSH의 모든 플래그를 사용할 수 있습니다.
> 더 많은 정보: <https://manned.org/autossh>.

- SSH session을 열고, 모니터링 포트가 데이터를 리턴하지 못하면 다시 시작:

`autossh -M {{모니터링_포트}} "{{ssh_명령어}}"`

- 로컬 포트를 원격 포트로 전달하는 SSH session을 열고 필요한 경우 다시 시작:

`autossh -M {{모니터링_포트}} -L {{로컬_포트}}:localhost:{{원격_포트}} {{사용자}}@{{호스트}}`

- ssh(백그라운드에서 실행)를 실행하기 전에 포크하고 원격 쉘을 열지 않는다:

`autossh -f -M {{모니터링_포트}} -N "{{ssh_명령어}}"`

- 모니터링 포트없이 백그라운드에서 autossh를 실행하는 대신 실패를 감지하기 위해 10초마다 SSH 연결 유지에 의존:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{ssh_명령어}}"`

- 모니터링 포트, 원격 쉘 없이 백그라운드에서 autossh를 실행하고, 포트 전달에 실패하면 종료:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{로컬_포트}}:localhost:{{원격_포트}} {{사용자}}@{{호스트}}`

- 디버그 출력이 파일에 기록되고, ssh 상세 출력이 두번째 파일에 기록 된 상태에서 백그라운드에서 autossh를 실행:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{로그_파일}} autossh -f -M {{모니터링_포트}} -v -E {{ssh_로그_파일}} {{ssh_명령어}}`
