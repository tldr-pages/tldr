# pgrep

> Find processes by name.
> More information: <https://keith.github.io/xcode-man-pages/pgrep.1.html>.

- Return PIDs of any running processes with a matching command string:

`pgrep {{process_name}}`

- Print the process name in addition to the PID ([l]ong output):

`pgrep -l {{process_name}}`

- Match processes against the [f]ull argument list instead of just the process name:

`pgrep -f "{{process_name}} {{parameter}}"`

- Print the PID together with the [f]ull argument [l]ist for each match:

`pgrep -fl "{{process_name}}"`

- Search for processes run by a specific [u]ser (effective UID):

`pgrep -u {{username}} {{process_name}}`

- Select only the [n]ewest (most recently started) matching process:

`pgrep -n {{process_name}}`
