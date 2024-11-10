# xfce4-terminal

> XFCE4 터미널 에뮬레이터.
> 더 많은 정보: <https://docs.xfce.org/apps/xfce4-terminal/start>.

- 새 터미널 창 열기:

`xfce4-terminal`

- 초기 제목 설정:

`xfce4-terminal --initial-title "{{초기_제목}}"`

- 현재 터미널 창에 새 탭 열기:

`xfce4-terminal --tab`

- 새 터미널 창에서 명령어 실행:

`xfce4-terminal --command "{{명령어_및_인수}}"`

- 실행한 명령어가 완료된 후에도 터미널 유지:

`xfce4-terminal --command "{{명령어_및_인수}}" --hold`

- 여러 새 탭을 열고 각 탭에서 명령어 실행:

`xfce4-terminal --tab --command "{{명령어1}}" --tab --command "{{명령어2}}"`
