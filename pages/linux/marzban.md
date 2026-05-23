# marzban

> Manage Marzban proxy server users, admins, subscriptions, and shell completions.
> More information: <https://github.com/Gozargah/Marzban/blob/master/cli/README.md>.

- Create a sudo admin, using an environment variable for the password:

`MARZBAN_ADMIN_PASSWORD={{password}} marzban cli admin create --username {{admin}} --sudo`

- List admins:

`marzban cli admin list`

- List users, optionally filtering by username, note, status, or owner admin:

`marzban cli user list --username {{username}} --search {{text}} --status {{active|disabled|limited|expired|on_hold}} --owner {{admin}}`

- Transfer a user's ownership to another admin, skipping confirmations:

`marzban cli user set-owner --username {{username}} --owner {{admin}} --yes`

- Generate a user's subscription config and write it to a file:

`marzban cli subscription get-config --username {{username}} --format {{v2ray|clash}} --output {{path/to/file}}`
