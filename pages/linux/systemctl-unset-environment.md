# systemctl unset-environment

> Unset one or more service manager environment variables.
> This undoes the effect of `systemctl set-environment`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#unset-environment%20VARIABLE%E2%80%A6>.

- Unset a single environment variable:

`systemctl unset-environment {{var}}`

- Unset multiple environment variables at once:

`systemctl unset-environment {{var1 var2 ...}}`

- Unset an environment variable in the user service manager:

`systemctl unset-environment {{var}} --user`
