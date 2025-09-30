# startx

> 단일 X 윈도우 시스템 세션 실행을 위한 사용자 인터페이스를 제공하는 `xinit`의 프론트엔드.
> 더 많은 정보: <https://x.org/releases/X11R7.5/doc/man/man1/startx.1.html>.

- X 세션 시작:

`startx`

- 미리 정의된 깊이 값으로 X 세션 시작:

`startx -- -depth {{값}}`

- 미리 정의된 DPI 값으로 X 세션 시작:

`startx -- -dpi {{값}}`

- `.xinitrc` 파일의 설정을 무시하고 새 X 세션 시작:

`startx /{{경로/대상/윈도우_매니저_또는_데스크톱_환경}}`
