# systemctl import-environment

> Import environment variables from the shell into systemd's environment.
> See also: `show-environment`, `unset-environment`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#%0A%20%20%20%20%20%20%20%20%20%20%20%20import-environment%0A%20%20%20%20%20%20%20%20%20%20%20%20VARIABLE%E2%80%A6%0A%20%20%20%20%20%20%20%20%20%20>.

- Import a varaible:

`systemctl import-environment {{variable}}`

- Import multiple variables:

`systemctl import-environment {{variable_1 variable_2 ...}}`

- Import variables for user services:

`systemctl import-environment {{variable}} --user`
