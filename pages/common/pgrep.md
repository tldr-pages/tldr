# pgrep

> Find or signal processes by name.
> More information: <https://manned.org/pgrep>.

- Return PIDs of any running processes with a matching command string:

`pgrep {{process_name}}`

- Search for processes including their command-line options:

`pgrep {{[-f|--full]}} "{{process_name}} {{parameter}}"`

- Search for processes run by a specific user:

`pgrep {{[-u|--euid]}} root {{process_name}}`
