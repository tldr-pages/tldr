# systemctl set-environment

> Set one or more service manager environment variables.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#set-environment%20VARIABLE=VALUE%E2%80%A6>.

- Set a single environment variable:

`systemctl set-environment {{var value}}`

- Set multiple environment variables at once:

`systemctl set-environment {{var1 value1 var2 value2 ...}}`

- Set an environment variable for the user service manager:

`systemctl set-environment {{var value}} --user`
