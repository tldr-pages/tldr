# aa-logprof

> Interactively update AppArmor security profiles based on logged violations.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-logprof.8>.

- Interactively review and update profiles based on system logs:

`sudo aa-logprof`

- Use a specific directory for AppArmor profiles:

`sudo aa-logprof {{[-d|--dir]}} {{/path/to/profiles}}`

- Use a specific log file instead of the default:

`sudo aa-logprof {{[-f|--file]}} {{/path/to/logfile}}`

- Ignore all log entries before the specified mark:

`sudo aa-logprof {{[-m|--logmark]}} "{{log_marker_text}}"`

- Display help:

`aa-logprof {{[-h|--help]}}`
