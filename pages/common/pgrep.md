# pgrep

> Find or signal process by name.
> More information: <https://www.man7.org/linux/man-pages/man1/pkill.1.html>.

- Return PIDs of any running processes with a matching command string:

`pgrep {{process_name}}`

- Search full command line with parameters instead of just the process name:

`pgrep --full "{{process_name}} {{parameter}}"`

- Search for process run by a specific user:

`pgrep --euid root {{process_name}}`
