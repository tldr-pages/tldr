# xkill

> 그래픽 세션에서 창을 대화식으로 종료.
> 같이 보기: `kill`, `killall`.
> 더 많은 정보: <https://www.x.org/releases/current/doc/man/man1/xkill.1.xhtml>.

- 왼쪽 마우스 버튼을 눌러 창을 종료할 수 있는 커서 표시 (다른 마우스 버튼을 눌러 취소):

`xkill`

- 마우스 버튼을 눌러 종료할 창을 선택할 수 있는 커서 표시:

`xkill -button any`

- 특정 ID를 가진 창 종료 (`xwininfo`를 사용하여 창 정보를 얻을 수 있음):

`xkill -id {{id}}`
