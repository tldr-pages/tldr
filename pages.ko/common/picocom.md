# picocom

> 직렬 콘솔을 에뮬레이션 하는 최소한의 프로그램.
> 관련 항목: `minicom`, `cu`, `tio`.
> 더 많은 정보: <https://manned.org/picocom>.

- 기본 baud rate 9600으로 직렬 콘솔 연결:

`sudo picocom {{/dev/ttyXYZ}}`

- 지정한 baud rate로 직렬 콘솔 연결:

`sudo picocom {{/dev/ttyXYZ}} {{[-b|--baud]}} {{baud_rate}}`

- 특수문자 매핑 설정 (예: `LF`를 `CRLF`으로 변환):

`sudo picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`

- picocom 종료:

`<Ctrl a><Ctrl x>`

- 도움말 표시:

`picocom {{[-h|--help]}}`
