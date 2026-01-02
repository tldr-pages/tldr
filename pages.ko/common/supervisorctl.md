# supervisorctl

> Supervisor는 UNIX 계열 운영 체제에서 여러 프로세스를 제어할 수 있게 해주는 클라이언트/서버 시스템입니다.
> Supervisorctl은 shell과 유사한 인터페이스를 제공하는 supervisor의 명령줄 클라이언트입니다.
> 더 많은 정보: <https://supervisord.org/running.html#running-supervisorctl>.

- 프로세스의 상태 표시 (`process_name`이 지정되지 않으면 모든 프로세스 표시):

`supervisorctl status {{프로세스_이름}}`

- 프로세스 시작/중지/재시작:

`supervisorctl {{start|stop|restart}} {{프로세스_이름}}`

- 그룹 내 모든 프로세스 시작/중지/재시작:

`supervisorctl {{start|stop|restart}} {{그룹_이름}}:*`

- 프로세스 `stderr`의 마지막 100바이트 표시:

`supervisorctl tail -100 {{프로세스_이름}} stderr`

- 프로세스의 `stdout` 계속 표시:

`supervisorctl tail -f {{프로세스_이름}} stdout`

- 프로세스 구성 파일을 다시 로드하여 필요한 경우 프로세스를 추가/제거:

`supervisorctl update`
