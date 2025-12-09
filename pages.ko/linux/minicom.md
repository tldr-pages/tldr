# minicom

> 디바이스의 직렬 인터페이스와 통신.
> 더 많은 정보: <https://manned.org/minicom>.

- 특정 직렬 포트 열기:

`sudo minicom {{[-D|--device]}} {{/dev/ttyUSB0}}`

- 특정 직렬 포트를 주어진 보율로 열기:

`sudo minicom {{[-D|--device]}} {{/dev/ttyUSB0}} {{[-b|--baudrate]}} {{115200}}`

- 특정 직렬 포트와 통신하기 전에 설정 메뉴로 들어가기:

`sudo minicom {{[-D|--device]}} {{/dev/ttyUSB0}} {{[-s|--setup]}}`
