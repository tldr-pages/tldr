# flock

> Manage locks from shell scripts.
> It can be used to ensure that only one process of a command is running.
> More information: <https://manned.org/flock>.

- Run a command with a file lock as soon as the lock is not required by others:

`flock {{path/to/lock.lock}} --command "{{command}}"`

- Run a command with a file lock, and exit if the lock doesn't exist:

`flock {{path/to/lock.lock}} --nonblock --command "{{command}}"`

- Run a command with a file lock, and exit with a specific error code if the lock doesn't exist:

`flock {{path/to/lock.lock}} --nonblock --conflict-exit-code {{error_code}} -c "{{command}}"`
