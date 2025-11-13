# dunstify

> `notify-send`의 확장 기능을 가진 알림 도구로, `dunst`를 중심으로 더 많은 기능을 제공합니다.
> `notify-send`의 모든 옵션을 수용합니다.
> 더 많은 정보: <https://dunst-project.org/documentation/dunstify>.

- 지정된 제목과 메시지로 알림 표시:

`dunstify "{{제목}}" "{{메시지}}"`

- 지정된 긴급도로 알림 표시:

`dunstify "{{제목}}" "{{메시지}}" -u {{low|normal|critical}}`

- 메시지 ID 지정 (같은 ID의 이전 메시지를 덮어씀):

`dunstify "{{제목}}" "{{메시지}}" -r {{123}}`

- 도움말 표시:

`dunstify --help`
