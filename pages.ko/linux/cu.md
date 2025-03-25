# cu

> 다른 시스템에 연결하여 다이얼인/직렬 터미널 역할을 하거나 오류 검사가 없는 파일 전송을 수행합니다.
> 더 많은 정보: <https://manned.org/cu>.

- 주어진 직렬 포트 열기:

`sudo cu {{[-l|--line]}} {{/dev/ttyUSB0}}`

- 주어진 보율로 주어진 직렬 포트 열기:

`sudo cu {{[-l|--line]}} {{/dev/ttyUSB0}} {{[-s|--speed]}} {{115200}}`

- 주어진 보율로 주어진 직렬 포트를 열고 문자를 로컬에서 에코(반이중 모드):

`sudo cu {{[-l|--line]}} {{/dev/ttyUSB0}} {{[-s|--speed]}} {{115200}} {{[-h|--halfduplex]}}`

- 주어진 보율, 패리티, 하드웨어 또는 소프트웨어 흐름 제어 없이 주어진 직렬 포트 열기:

`sudo cu {{[-l|--line]}} {{/dev/ttyUSB0}} {{[-s|--speed]}} {{115200}} --parity={{even|odd|none}} {{[-f|--nortscts]}} --nostop`

- 연결 중 `cu` 세션 종료:

`<Enter><~><.>`
