# autossh

> SSH 연결을 실행, 모니터링 및 재시작. port 재전송 tunnel을 유지하기 위해 자동 재연결. 모든 SSH 플래그 허용.
> 더 많은 정보: <https://www.harding.motd.ca/autossh>.

- SSH session을 열고, 모니터링 포트가 데이터를 리턴하지 못하면 다시 시작:

`autossh -M {{monitor_port}} "{{ssh_command}}"`

- 로컬 포트를 원격 포트로 전달하는 SSH session을 열고 필요한 경우 다시 시작:

`autossh -M {{monitor_port}} -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- ssh(백그라운드에서 실행)를 실행하기 전에 포크하고 원격 쉘을 열지 않는다:

`autossh -f -M {{monitor_port}} -N "{{ssh_command}}"`

- 모니터링 포트없이 백그라운드에서 autossh를 실행하는 대신 실패를 감지하기 위해 10초마다 SSH 연결 유지에 의존:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{ssh_command}}"`

- 모니터링 포트, 원격 쉘 없이 백그라운드에서 autossh를 실행하고, 포트 전달에 실패하면 종료:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- 디버그 출력이 파일에 기록되고 ssh 상세 출력이 두번째 파일에 기록 된 상태에서 백그라운드에서 autossh를 실행:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{log_file}} autossh -f -M {{monitor_port}} -v -E {{ssh_log_file}} {{ssh_command}}`
