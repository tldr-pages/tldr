# pgrep

> Find or signal processes by name.
> More information: <https://www.manned.org/pgrep>.

- Return PIDs of any running processes with a matching command string:

`pgrep {{process_name}}`

- Search for processes including their command-line options:

`pgrep --full "{{process_name}} {{parameter}}"`

- Search for processes run by a specific user:

`pgrep --euid root {{process_name}}`
