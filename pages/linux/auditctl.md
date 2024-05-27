# auditctl
> Utility to control the behavior, get status and manage rules of the Linux Auditing System.
> More information: <https://manned.org/auditctl>.

- Display the [s]tatus of the audit system:

`auditctl -s`

- [l]ist all currently loaded audit rules:

`auditctl -l`

- [D]elete all audit rules:

`auditctl -D`

- [e]nable/disable the audit system:

`auditctl -e {{1|0}}`

- Watch a file for changes:

`auditctl -a always,exit -F arch=b64 -F path={{/path/to/file}} -F perm=wa`

- Recursively watch a directory for changes:

`auditctl -a always,exit -F arch=b64 -F dir={{/path/to/directory/}} -F perm=wa`

- Display [h]elp:

`auditctl -h`
