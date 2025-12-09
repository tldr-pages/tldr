# wofi

> wlroots 기반 Wayland 컴포지터를 위한 애플리케이션 실행기로, `rofi` 및 `dmenu`와 유사합니다.
> 더 많은 정보: <https://manned.org/wofi>.

- 앱 목록 표시:

`wofi {{[-S|--show]}} drun`

- 모든 명령 목록 표시:

`wofi {{[-S|--show]}} run`

- 항목 목록을 `stdin`으로 전달하고 선택한 항목을 `stdout`으로 출력:

`printf "{{선택1\n선택2\n선택3}}" | wofi {{[-d|--dmenu]}}`
