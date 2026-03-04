# ohdear

> The official Oh Dear CLI.
> More information: <https://github.com/ohdearapp/ohdear-cli>.

- Display details about the currently authenticated user:

`ohdear-cli get-me`

- Add a new monitor to Oh Dear:

`ohdear create-monitor --field "team_id={{team_id}}" --field "type={{http|ping|tcp}}" --field "url={{url}}"`

- Display a list of monitors and their current status:

`ohdear list-monitors`

- Display details about a specific monitor:

`ohdear get-monitor --monitor-id {{monitor_id}}`
