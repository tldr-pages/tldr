# supervisord

> Supervisor is a client/server system for controlling some processes on UNIX-like operating systems.
> Supervisord is the server part of supervisor; it is primarily managed via a configuration file.
> More information: <https://supervisord.org/running.html#running-supervisord>.

- Start `supervisord` with specified configuration file:

`supervisord {{[-c|--configuration]}} {{path/to/file}}`

- Run supervisord in the foreground:

`supervisord {{[-n|--nodaemon]}}`
