# top

> Display dynamic real-time information about running processes.

- Start top:

`top`

- Do not show any idle or zombie processes:

`top -i`

- List processes owned by given user:

`top -u {{user-name}}`

- List processes by PID. It takes a comma separated list. (Normally you wouldn't know PIDs off hand. This example picks the PIDs from the process name):

`top -p $(pgrep -d ',' {{nginx}})`

- Get help about interactive commands:

`?`
