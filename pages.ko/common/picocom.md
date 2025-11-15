# picocom

> 시리얼 콘솔을 에뮬레이트하기 위한 최소한의 프로그램.
> 더 많은 정보: <https://manned.org/picocom>.

- 지정된 전송 속도로 시리얼 콘솔에 연결:

`picocom {{/dev/ttyXYZ}} {{[-b|--baud]}} {{전송_속도}}`

- 특수 문자 매핑 (예: `LF`를 `CRLF`로):

`picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`
