# runsvdir

> Run an entire directory of services.
> More information: <https://manpages.ubuntu.com/manpages/latest/man8/runsvdir.8.html>.

- Start and manage all services in a directory as the current user:

`runsvdir {{path/to/services}}`

- Start and manage all services in a directory as root:

`sudo runsvdir {{path/to/services}}`

- Start services in separate sessions:

`runsvdir -P {{path/to/services}}`
