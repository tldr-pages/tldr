# frida-ps

> 로컬 또는 원격 장치의 프로세스 목록 표시.
> 더 많은 정보: <https://frida.re/docs/frida-ps/>.

- 로컬 머신에서 실행 중인 모든 프로세스 목록 표시:

`frida-ps`

- USB로 연결된 장치에서 실행 중인 모든 프로세스 목록 표시:

`frida-ps {{[-U|--usb]}}`

- USB로 연결된 장치에서 실행 중인 모든 애플리케이션 목록 표시:

`frida-ps {{[-U|--usb]}} {{[-a|--applications]}}`

- USB로 연결된 장치에 설치된 모든 애플리케이션 목록 표시:

`frida-ps {{[-U|--usb]}} {{[-i|--installed]}}`

- 특정 장치의 프로세스 목록 표시:

`frida-ps {{[-D|--device]}} {{장치_아이디}}`
