# talk

> 시각적 커뮤니케이션 프로그램으로, 사용자의 터미널에서 다른 사용자의 터미널로 라인을 복사합니다.
> 더 많은 정보: <https://www.gnu.org/software/inetutils/manual/inetutils.html#talk-invocation>.

- 동일한 기기에서 사용자의 talk 세션 시작:

`talk {{사용자명}}`

- 동일한 기기의 tty3에 로그인된 사용자와 talk 세션 시작:

`talk {{사용자명}} {{tty3}}`

- 원격 기기의 사용자와 talk 세션 시작:

`talk {{사용자명}}@{{호스트명}}`

- 양쪽 터미널 화면의 텍스트 지우기:

`<Ctrl d>`

- talk 세션 종료:

`<Ctrl c>`
