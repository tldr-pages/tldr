# pio device

> PlatformIO 장치를 관리하고 모니터링.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/device/>.

- 사용 가능한 모든 시리얼 포트 나열:

`pio device list`

- 사용 가능한 모든 논리 장치 나열:

`pio device list --logical`

- 대화형 장치 모니터 시작:

`pio device monitor`

- 특정 포트를 수신하며 대화형 장치 모니터 시작:

`pio device monitor --port {{/dev/ttyUSBX}}`

- 특정 전송 속도를 설정하여 대화형 장치 모니터 시작 (기본값은 9600):

`pio device monitor --baud {{57600}}`

- 특정 EOL 문자를 설정하여 대화형 장치 모니터 시작 (기본값은 `CRLF`):

`pio device monitor --eol {{CRLF|CR|LF}}`

- 대화형 장치 모니터 메뉴로 이동:

`<Ctrl t>`
