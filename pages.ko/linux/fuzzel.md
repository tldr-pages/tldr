# fuzzel

> Wayland 환경에서 동작하는 애플리케이션 실행기 및 퍼지 검색 도구(`rofi`와 `dmenu`에서 영감을 받아 만들어짐).
> 더 많은 정보: <https://codeberg.org/dnkl/fuzzel>.

- 애플리케이션 실행:

`fuzzel`

- dmenu 모드로 `fuzzel` 실행:

`fuzzel {{[-d|--dmenu]}}`

- `ls` 명령의 출력을 메뉴로 표시:

`{{ls}} | fuzzel {{[-d|--dmenu]}}`

- 줄바꿈으로(`\n`) 구분된 사용자 지정 항목을 메뉴로 표시:

`echo -e "{{red}}\n{{green}}\n{{blue}}" | fuzzel {{[-d|--dmenu]}}`

- 여러 항목 중 사용자가 선택한 값을 파일에 저장:

`echo -e "{{red}}\n{{green}}\n{{blue}}" | fuzzel {{[-d|--dmenu]}} > {{color.txt}}`

- 애플리케이션 사용 횟수 캐시 초기화 (기본 캐시 디렉터리: `$XDG_CACHE_HOME/fuzzel`):

`rm {{[-v|--verbose]}} $HOME/.cache/fuzzel`

- 지정한 모니터에서 `fuzzel` 실행 (`wlr-randr` 또는 `swaymsg --type get_outputs` 참고):

`fuzzel {{[-o|--output]}} "{{DP-1}}"`

- `fuzzel`를 사용하여 온라인 검색 수행:

`fuzzel {{[-d|--dmenu]}} {{[-l|--lines]}} 0 --placeholder "{{Type your search}}" | sed 's/^/\"/g;s/$/\"/g' | xargs firefox --search`
