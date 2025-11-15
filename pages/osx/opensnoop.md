# opensnoop

> Track file opens on your system.
> More information: <https://keith.github.io/xcode-man-pages/opensnoop.1m.html>.

- Print all file opens as they occur:

`sudo opensnoop`

- Track all file opens by a process by name:

`sudo opensnoop -n "{{process_name}}"`

- Track all file opens by a process by PID:

`sudo opensnoop -p {{PID}}`

- Track which processes open a specified file:

`sudo opensnoop -f {{path/to/file}}`
