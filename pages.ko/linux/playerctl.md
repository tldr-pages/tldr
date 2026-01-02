# playerctl

> MPRIS를 통해 미디어 플레이어 제어.
> 더 많은 정보: <https://github.com/altdesktop/playerctl#using-the-cli>.

- 재생/일시정지 전환:

`playerctl play-pause`

- 다음 트랙으로 건너뛰기:

`playerctl next`

- 이전 트랙으로 돌아가기:

`playerctl previous`

- 모든 플레이어 나열:

`playerctl --list-all`

- 특정 플레이어에 명령 전송:

`playerctl --player {{플레이어_이름}} {{play-pause|next|previous|...}}`

- 모든 플레이어에 명령 전송:

`playerctl --all-players {{play-pause|next|previous|...}}`

- 현재 트랙에 대한 메타데이터 표시:

`playerctl metadata --format "{{현재 재생 중: \{\{artist\}\} - \{\{album\}\} - \{\{title\}\}}}"`
