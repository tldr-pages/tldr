# watch

> Execute a program periodically and monitor the output in full-screen mode.
> More information: <https://manned.org/watch>.

- Repeatedly run a command and show the result:

`watch {{command}}`

- Re-run a command every 60 seconds:

`watch --interval {{60}} {{command}}`

- Monitor disk space, highlighting differences as they appear:

`watch --differences {{df}}`

- Repeatedly run a pipeline and show the result:

`watch "{{command_1}} | {{command_2}} | {{command_3}}"`

- Exit `watch` if the visible output changes:

`watch --chgexit {{lsblk}}`

- Interpret terminal control characters:

`watch --color {{ls --color=always}}`
