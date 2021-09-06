# daemonize

> Run a command (that does not daemonize itself) as a Unix daemon.
> More information: <http://software.clapper.org/daemonize/>.

- Run a command as a daemon:

`daemonize {{command}} {{command_arguments}}`

- Write the PID to the specified file:

`daemonize -p {{path/to/pidfile}} {{command}} {{command_arguments}}`

- Use a lock file to ensure that only one instance runs at a time:

`daemonize -l {{path/to/lockfile}} {{command}} {{command_arguments}}`

- Use the specified user account:

`sudo daemonize -u {{user}} {{command}} {{command_arguments}}`
