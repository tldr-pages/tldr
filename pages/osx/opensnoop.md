# opensnoop

> Tool that tracks file opens on your system.

- Print all file opens as they occur:

`sudo opensnoop`

- Track all file opens by a process by name:

`sudo opensnoop -n {{YourProcess}}`

- Track all file opens by a process by PID:

`sudo opensnoop -p {{YourPID}}`

- Track which processes open a specified file:

`sudo opensnoop -f {{YourFile}}`
