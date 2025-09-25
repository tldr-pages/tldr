# watch

> Execute a program periodically and monitor the output in full-screen mode.
> More information: <https://manned.org/watch>.

- Repeatedly run a command and show the result:

`watch {{command}}`

- Re-run a command every 60 seconds:

`watch {{[-n|--interval]}} 60 {{command}}`

- Monitor disk space, highlighting differences as they appear:

`watch {{[-d|--differences]}} df`

- Repeatedly run a pipeline and show the result:

`watch "{{command1}} | {{command2}} | {{command3}}"`

- Exit `watch` if the visible output changes:

`watch {{[-g|--chgexit]}} {{lsblk}}`

- Interpret terminal control characters:

`watch {{[-c|--color]}} {{ls --color=always}}`
