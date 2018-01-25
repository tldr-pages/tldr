# tasklist

> Display a list of currently running processes on a local or remote machine.

- Display currently running processes:

`tasklist`

- Display running processes in the specified output format (`table`, `list`, or `csv`):

`tasklist /fo {{format}}`

- Display running processes using the specified module name:

`tasklist /m {{module_pattern}}`

- Display processes running on a remote machine:

`tasklist /s {{remote_name}} /u {{username}} /p {{password}}`

- Display services using each process:

`tasklist /svc`
