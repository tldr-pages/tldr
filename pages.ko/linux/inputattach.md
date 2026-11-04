# inputattach

> 장치를 Linux 입력 시스템에 연결함.
> 입력 장치는 `/dev/input/` 아래 파일로 제공됨.
> 더 많은 정보: <https://manned.org/inputattach>.

- Pulse8 CEC 장치를 입력 시스템에 연결:

`inputattach --pulse8-cec {{/dev/ttyACM0}}`

- 도움말 표시:

`inputattach --help`
