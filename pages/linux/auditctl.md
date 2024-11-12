# auditctl

> Utility to control the behavior, get status and manage rules of the Linux Auditing System.
> More information: <https://manned.org/auditctl>.

- Display the [s]tatus of the audit system:

`sudo auditctl -s`

- [l]ist all currently loaded audit rules:

`sudo auditctl -l`

- [D]elete all audit rules:

`sudo auditctl -D`

- [e]nable/disable the audit system:

`sudo auditctl -e {{1|0}}`

- Watch a file for changes:

`sudo auditctl -a always,exit -F arch=b64 -F path={{/path/to/file}} -F perm=wa`

- Recursively watch a directory for changes:

`sudo auditctl -a always,exit -F arch=b64 -F dir={{/path/to/directory/}} -F perm=wa`

- Display [h]elp:

`auditctl -h`
