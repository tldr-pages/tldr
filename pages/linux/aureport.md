# aureport

> Generate summary reports of auditd logs.
> More information: <https://manned.org/aureport>.

- Display a summary of auditd events:

`sudo aureport`

- Generate a summary of login events:

`sudo aureport {{[-l|--login]}}`

- List all syscall reports:

`sudo aureport {{[-s|--syscall]}}`

- Generate a summary of executable events:

`sudo aureport {{[-x|--executable]}}`

- Show a summary of events for a specific time range:

`sudo aureport {{[-ts|--start]}} {{start_time}} {{[-te|--end]}} {{end_time}}`

- List all audit files and the time range of events they cover:

`sudo aureport {{[-t|--log-time]}}`

- Display help:

`aureport --help`
