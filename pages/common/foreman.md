# foreman

> Foreman manages Procfile-based applications
> Foreman supports exports to: bluepill, inittab, launchd, runit, supervisord, systemd, and upstart

- Run one instance of each type of process defined in your Procfile:

`foreman start {{process}}`

- Run one instance of the specified application type:

`foreman start {{process}}`

- Run one-off commands using the same environment as your defined processes:

`foreman run {{command}}`

- Export application to another process management format by path:

`foreman export {{format}} {{path/to/app/root}}`

- Export application to another process management format by app name:

`foreman export {{format}} --app {{app_name}}`
