# systemd-cat

> Connect a pipeline or program's output streams with the systemd journal.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-cat.html>.

- Write the output of the specified command to the journal (both output streams are captured):

`systemd-cat {{command}}`

- Write the output of a pipeline to the journal (`stderr` stays connected to the terminal):

`{{command}} | systemd-cat`

- Use the specified identifier (default: `cat` when reading from a pipeline, executable name otherwise):

`{{command}} | systemd-cat {{[-t|--identifier]}} {{id}}`

- Use the specified default priority level for all logged messages:

`systemd-cat {{[-p|--priority]}} {{emerg|alert|crit|err|warning|notice|info|debug}} {{command}}`

- Use the specified default priority level for the logged messages from the command's `stderr`:

`systemd-cat --stderr-priority {{emerg|alert|crit|err|warning|notice|info|debug}} {{command}}`
