# cec-client

> 직렬 버스 CEC 연결 관리.
> 관련 항목: `cec-ctl`.
> 더 많은 정보: <https://manned.org/cec-client>.

- 모든 CEC 어댑터 목록 표시:

`cec-client {{[-l|--list-devices]}}`

- 대화형 CEC 세션 시작:

`sudo cec-client`

- On-Screen Display 이름 설정:

`sudo cec-client {{[-o|--osd-name]}} {{이름}}`

- 단일 명령 전송:

`echo {{on 0}} | sudo cec-client {{[-s|--single-command]}}`

- 대화형 모드에서 장치를 대기(standby) 상태로 전환:

`standby {{0}}`

- 대화형 모드에서 장치 전원 켜기:

`on {{0}}`
