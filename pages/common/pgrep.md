# pgrep

> Find or signal process by name.

- Return PIDs of any running processes with a matching command string:

`pgrep {{process_name}}`

- Search full command line with parameters instead of just the process name:

`pgrep -f "{{process_name}} {{parameter}}"`

- Search for process run by a specific user:

`pgrep -u root {{process_name}}`
