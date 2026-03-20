# ohdear

> 공식 Oh Dear CLI.
> 더 많은 정보: <https://ohdear.app/docs/tools-and-sdks/our-cli-tool#available-commands>.

- 현재 인증된 사용자에 대한 상세 정보를 표시:

`ohdear get-me`

- Oh Dear에 새로운 모니터를 추가:

`ohdear create-monitor --field "team_id={{팀_id}}" --field "type={{http|ping|tcp}}" --field "url={{url}}"`

- 모니터 목록과 현재 상태를 표시:

`ohdear list-monitors`

- 특정 모니터의 상세 정보를 표시:

`ohdear get-monitor --monitor-id {{모니터_id}}`
