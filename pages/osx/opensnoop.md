# opensnoop

> Tool that tracks file opens on your system.

- Prints all file opens as they occur:

`sudo opensnoop`

- Tracks all file opens by a process by name:

`sudo opensnoop -n {{YourProcess}}`

- Tracks all file opens by a process by PID:

`sudo opensnoop -p {{YourPID}}`

- Tracks which processes open a specified file:

`sudo opensnoop -f {{YourFile}}`
