# rofi

> 애플리케이션 실행기 및 창 전환기.
> 더 많은 정보: <https://github.com/davatorium/rofi#manpage>.

- 앱 목록 표시:

`rofi -show drun`

- 모든 명령 목록 표시:

`rofi -show run`

- 창 간 전환:

`rofi -show window`

- 항목 목록을 `stdin`으로 전달하고 선택한 항목을 `stdout`으로 출력:

`printf "{{선택1\n선택2\n선택3}}" | rofi -dmenu`
