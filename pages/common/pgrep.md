# pgrep

> Find or signal process by name

- return PIDs of any running processes with a matching command string

`pgrep {{Finder}}`

- search full command line with parameters instead of just the process name

`pgrep -f "{{ssh root}}"`

- search for process run by a specific user

`pgrep -u root {{firefox}}`

- kill all processes which match

`pkill -9 {{Finder}}`
