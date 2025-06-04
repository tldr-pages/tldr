# xvfb-run

> 가상 X 서버 환경에서 명령 실행.
> 더 많은 정보: <https://manned.org/xvfb-run>.

- 가상 X 서버에서 지정된 명령 실행:

`xvfb-run {{명령}}`

- 기본값(99)이 사용 불가능한 경우, 사용 가능한 서버 번호를 자동으로 선택:

`xvfb-run {{[-a|--auto-servernum]}} {{명령}}`

- Xvfb 서버에 인수 전달:

`xvfb-run {{[-s|--server-args]}} "{{-screen 0 1024x768x24}}" {{명령}}`
