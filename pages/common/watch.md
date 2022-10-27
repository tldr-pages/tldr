# watch

> Execute a program periodically, showing output fullscreen.
> More information: <https://manned.org/watch>.

- Repeatedly run a command and show the result:

`watch {{command}}`

- Re-run a command every 60 seconds:

`watch -n {{60}} {{command}}`

- Monitor the contents of a directory, highlighting differences as they appear:

`watch -d {{ls -l}}`

- Repeatedly run a pipeline and show the result:

`watch '{{command_1}} | {{command_2}} | {{command_3}}'`
