# systemctl set-environment

> Set one or more service manager environment variables.
> These variables are stored in a separate environment block, combined with others when services are started.
> Added in version 233.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#set-environment%20VARIABLE%3DVALUE%E2%80%A6>.

- Set a single environment variable:

`systemctl set-environment {{var value}}`

- Set multiple environment variables at once:

`systemctl set-environment {{var1 value1 var2 value2 ...}}`

- Set an environment variable for the user service manager:

`systemctl --user set-environment {{var value}}`
