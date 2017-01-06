# supervisord

> Supervisor is a client/server system that allows its users to control a number of processes on UNIX-like operating systems.
> Supervisord is the server piece of supervisor, Most of supervisord's config should be placed in configuration file, some basic usage will be listed here.

- Start supervisord with specified configuration file:

`supervisord -c {{path/to/file}}`

- Run supervisord in the foreground:

`supervisord -n`
