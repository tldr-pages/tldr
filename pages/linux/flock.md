# flock

> Manage locks from shell scripts.
> You can use it to ensure that only one progress of your command is running.

- Run a command with a file lock, wait if the lock is required by others:

`flock /tmp/lock.lock -c "execute some command"`

- Run a command with a file lock, if the lock exists. Else exist:

`flock /tmp/lock.lock -n -c "execute some command"`

- Run a command with a file lock, if the lock exists. Else exist with errorcode:

`flock /tmp/lock.lock -n -E <errorcode> -c "execute some command"`
