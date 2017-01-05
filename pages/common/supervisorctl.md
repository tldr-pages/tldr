# supervisorctl

> Supervisor is a client/server system that allows its users to control a number of processes on UNIX-like operating systems.
> Supervisorctl command-line client piece of the supervisor which provides a shell-like interface.

- Start/stop/restart a process:

`supervisorctl {{action}} {{process name}}`

- Start/stop/restart all processes in a group:

`supervisorctl {{action}} {{group name}}:*`

- Tail last N **bytes** of process stderr:

`supervisorctl tail -{{N}} {{process name}} stderr`

- Continuous tail of named process stdout:

`supervisorctl tail -f {{process name}} stdout`

- Reload process config file to add/remove process as necessary:

`supervisorctl update`
