# frida-trace

> 함수 호출을 동적으로 추적하는 도구.
> 더 많은 정보: <https://frida.re/docs/frida-trace/>.

- 프로세스에서 패턴과 일치하는 모든 함수 추적:

`frida-trace {{[-i|--include]}} "{{와일드카드}}" {{프로세스_이름}}`

- 프로세스에서 특정 함수 추적:

`frida-trace {{[-i|--include]}} "{{함수_이름}}" {{프로세스_이름}}`

- 특정 모듈의 모든 함수 추적:

`frida-trace {{[-I|--include-module]}} "{{모듈_이름}}" {{프로세스_이름}}`

- USB로 연결된 장치에서 함수 추적:

`frida-trace {{[-U|--usb]}} {{[-i|--include]}} "{{함수_이름}}" {{프로세스_이름}}`

- 프로세스를 실행하면서 특정 함수 추적:

`frida-trace {{[-f|--file]}} {{경로/대상/실행파일}} {{[-i|--include]}} "{{함수_이름}}"`
