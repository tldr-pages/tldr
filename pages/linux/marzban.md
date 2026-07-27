# marzban

> Command-line tool for managing Marzban proxy servers.
> More information: <https://github.com/Gozargah/Marzban>.

- Create a new admin user:

`marzban admin create --username {{username}}`

- List all admin users:

`marzban admin list`

- Import the sudo admin from environment variables:

`marzban admin import-from-env`

- Delete an admin user:

`marzban admin delete --username {{username}}`

- Install shell completion for a specified shell:

`marzban completion install --shell {{bash|zsh|fish}}`
