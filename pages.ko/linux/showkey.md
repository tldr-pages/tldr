# showkey

> 키보드에서 누른 키의 키코드를 표시하여 키보드 관련 문제 디버깅 및 키 매핑에 유용합니다.
> 더 많은 정보: <https://manned.org/showkey>.

- 키코드를 10진수로 보기:

`sudo showkey`

- 스캔코드를 16진수로 표시:

`sudo showkey {{[-s|--scancodes]}}`

- 키코드를 10진수로 표시 (기본값):

`sudo showkey {{[-k|--keycodes]}}`

- 키코드를 ASCII, 10진수, 16진수로 표시:

`sudo showkey {{[-a|--ascii]}}`

- 프로그램 종료:

`<Ctrl d>`
