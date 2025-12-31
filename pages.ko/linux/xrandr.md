# xrandr

> 화면의 출력 크기, 방향 및/또는 반사를 설정.
> 더 많은 정보: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- 시스템의 현재 상태(알려진 화면, 해상도 등) 표시:

`xrandr {{[-q|--query]}}`

- 연결되지 않은 출력을 비활성화하고 기본 설정으로 연결된 출력 활성화:

`xrandr --auto`

- DisplayPort 1의 해상도와 갱신 빈도를 1920x1080, 60Hz로 변경:

`xrandr --output {{DP1}} --mode {{1920x1080}} --rate {{60}}`

- HDMI2의 해상도를 1280x1024로 설정하고 DP1의 오른쪽에 배치:

`xrandr --output {{HDMI2}} --mode {{1280x1024}} --right-of {{DP1}}`

- VGA1 출력 비활성화:

`xrandr --output {{VGA1}} --off`

- LVDS1의 밝기를 50%로 설정:

`xrandr --output {{LVDS1}} --brightness {{0.5}}`

- X 서버의 현재 상태 표시:

`xrandr {{[-d|--display]}} :{{0}} {{[-q|--query]}}`
