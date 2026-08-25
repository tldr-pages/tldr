# tuned

> Dynamic adaptive system tuning daemon.
> See also: `tuned-adm`.
> More information: <https://manned.org/tuned>.

- Start the `tuned` daemon in the foreground:

`sudo tuned`

- Start the `tuned` daemon in the background:

`sudo tuned {{[-d|--daemon]}}`

- Start the `tuned` daemon with a specific profile:

`sudo tuned {{[-p|--profile]}} {{profile_name}}`

- Start the `tuned` daemon logging to a custom log file:

`sudo tuned {{[-l|--log]}} {{path/to/log_file.log}}`

- Start the `tuned` daemon writing its process ID to a custom PID file:

`sudo tuned {{[-P|--pid]}} {{path/to/pid_file.pid}}`

- Start the `tuned` daemon with debugging messages:

`sudo tuned {{[-D|--debug]}}`
