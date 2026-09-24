# confettysh

> SSH 위에 애니메이션 색종이 및 불꽃놀이 효과 표시.
> 관련 항목: `ssh`.
> 더 많은 정보: <https://github.com/charmbracelet/confettysh>.

- 로컬 `confettysh` 서버 시작:

`confettysh`

- 사용자 지정 포트에서 서버 실행:

`confettysh {{[-p|--port]}} {{2323}}`

- 로컬 서버에 연결하여 불꽃놀이 표시:

`ssh {{[-p|--port]}} {{2222}} localhost -t fireworks`
