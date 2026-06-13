# frida

> 개발자, 리버스 엔지니어, 보안 연구자를 위한 동적 계측 툴킷.
> 더 많은 정보: <https://frida.re/docs/frida-cli/>.

- 실행 중인 프로세스에 연결된 대화형 쉘(REPL) 시작:

`frida {{프로세스_이름}}`

- USB를 통해 프로세스에 연결된 대화형 쉘 시작:

`frida {{[-U|--usb]}} {{프로세스_이름}}`

- PID를 사용하여 실행 중인 프로세스에 연결:

`frida {{[-p|--attach-pid]}} {{pid}}`

- 프로세스에 JavaScript 스크립트 로드:

`frida {{[-l|--load]}} {{경로/대상/스크립트.js}} {{프로세스_이름}}`

- Frida Codeshare <https://codeshare.frida.re/>에서 스크립트를 로드하여 프로세스에 적용:

`frida {{[-c|--codeshare]}} {{스크립트_이름}} {{프로세스_이름}}`
