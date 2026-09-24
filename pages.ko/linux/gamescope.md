# gamescope

> 게임 실행을 위한 micro-compositor.
> 관련 항목: `cage`.
> 더 많은 정보: <https://github.com/ValveSoftware/gamescope#keyboard-shortcuts>.

- gamescope를 사용해 프로그램 실행:

`gamescope -- {{프로그램}}`

- Steam을 통해 gamescope로 게임 실행:

`gamescope -- %command%`

- 720p 게임을 정수 스케일링으로 1440p까지 업스케일:

`gamescope {{[-h|--nested-height]}} 720 {{[-H|--output-height]}} 1440 {{[-S|--scaler]}} integer -- {{명령어}}`

- vsynce이 적용된 게임을 30 FPS로 제한:

`gamescope {{[-r|--nested-refresh]}} 30 -- {{명령어}}`

- Steam을 Big Picture 모드로 실행하고 gamescope와 통합:

`gamescope {{[-e|--steam]}} -- /usr/bin/steam -tenfoot`

- 우선 사용할 디스플레이 지정:

`gamescope {{[-O|--prefer-output]}} {{HDMI-A-1,DP-3,...}} -- {{program}}`

- 전체 화면 전환:

`<Super f>`

- 도움말 표시:

`gamescope --help`
