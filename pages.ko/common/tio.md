# tio

> 직렬 포트를 모니터링하고 상호작용.
> 관련 항목: `picocom`, `cu`, `minicom`.
> 더 많은 정보: <https://github.com/tio/tio#3-usage>.

- 기본 설정으로 직렬 포트 열기:

`tio {{/dev/ttyUSB0}}`

- 지정한 baud rate로 직렬 포트 열기:

`tio {{[-b|--baudrate]}} {{9600}} {{/dev/ttyUSB0}}`

- 직렬 포트를 열고 출력을 파일에 기록:

`tio {{[-L|--log]}} --log-file {{로그_파일}} {{/dev/ttyUSB0}}`

- 직렬 포트를 열고 16진수 출력 활성화:

`tio --output-mode hex {{/dev/ttyUSB0}}`

- 사용가능한 직렬 포트 목록 표시:

`tio {{[-l|--list]}}`

- `tio` 세션 종료:

`<Ctrl t><q>`
