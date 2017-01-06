# supervisorctl

> Supervisor is a client/server system that allows its users to control a number of processes on UNIX-like operating systems.
> Supervisorctl is the command-line client piece of the supervisor which provides a shell-like interface.

- Start/stop/restart a process:

`supervisorctl {{start|stop|restart}} {{process_name}}`

- Start/stop/restart all processes in a group:

`supervisorctl {{start|stop|restart}} {{group_name}}:*`

- Show last N **bytes** of process stderr:

`supervisorctl tail -{{N}} {{process_name}} stderr`

- Keep showing named process stdout until ctrl-c:

`supervisorctl tail -f {{process_name}} stdout`

- Reload process config file to add/remove processes as necessary:

`supervisorctl update`
