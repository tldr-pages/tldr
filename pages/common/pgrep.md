# pgrep

> Find or signal processes by name.
> More information: <https://www.man7.org/linux/man-pages/man1/pkill.1.html>.

- Return PIDs of any running processes with a matching command string:

`pgrep {{process_name}}`

- Search for processes including their command line options:

`pgrep --full "{{process_name}} {{parameter}}"`

- Search for processes run by a specific user:

`pgrep --euid root {{process_name}}`
