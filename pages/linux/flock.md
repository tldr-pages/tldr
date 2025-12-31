# flock

> Manage file locks from shell scripts.
> It can be used to ensure that only one instance of a command is running.
> More information: <https://manned.org/flock>.

- Run a command with a file lock as soon as the lock is available:

`flock {{path/to/lock.lock}} {{command}}`

- Run a command with a file lock, or exit if the lock is currently being held (with exit code 1):

`flock {{path/to/lock.lock}} {{[-n|--nonblock]}} {{command}}`

- Run a command with a file lock, or exit with a specific error code if the lock is currently being held:

`flock {{path/to/lock.lock}} {{[-n|--nonblock]}} {{[-E|--conflict-exit-code]}} {{123}} {{command}}`

- Run a command with a file lock, waiting up to 10 seconds for the lock to be available before giving up:

`flock {{path/to/lock.lock}} {{[-w|--timeout]}} 10 {{command}}`

- Backup a bunch of files, waiting for the previous `tar` command to finish if it's still running elsewhere and holding the same lock file (can be used in a `cron` job that runs often):

`flock {{path/to/backup.lock}} {{tar -cvf path/to/backup.tar path/to/data/}}`
