# rc-service

> 매개변수를 사용하여 OpenRC 서비스를 찾아 실행합니다.
> 같이 보기: `openrc`.
> 더 많은 정보: <https://manned.org/rc-service>.

- 서비스 상태 표시:

`rc-service {{서비스_이름}} status`

- 서비스 시작:

`sudo rc-service {{서비스_이름}} start`

- 서비스 중지:

`sudo rc-service {{서비스_이름}} stop`

- 서비스 재시작:

`sudo rc-service {{서비스_이름}} restart`

- 서비스의 사용자 지정 명령을 실행 시뮬레이션:

`sudo rc-service --dry-run {{서비스_이름}} {{명령_이름}}`

- 서비스의 사용자 지정 명령 실제 실행:

`sudo rc-service {{서비스_이름}} {{명령_이름}}`

- 디스크에서 서비스 정의 위치 확인:

`sudo rc-service --resolve {{서비스_이름}}`
