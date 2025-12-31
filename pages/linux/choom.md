# choom

> Display and change the adjust out-of-memory killer score.
> More information: <https://manned.org/choom>.

- Display the OOM-killer score of the process with a specific ID:

`choom {{[-p|--pid]}} {{pid}}`

- Change the adjust OOM-killer score of a specific process:

`choom {{[-p|--pid]}} {{pid}} {{[-n|--adjust]}} {{-1000..+1000}}`

- Run a command with a specific adjust OOM-killer score:

`choom {{[-n|--adjust]}} {{-1000..+1000}} {{command}} {{argument1 argument2 ...}}`
