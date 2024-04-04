# prosodyctl

> The control tool for the Prosody XMPP server.
> Note: process management through `prosodyctl` is discouraged. Instead, use the tools provided by your system (e.g. `systemctl`).
> More information: <https://prosody.im/doc/prosodyctl>.

- Show the status of the Prosody server:

`sudo prosodyctl status`

- Reload the server's configuration files:

`sudo prosodyctl reload`

- Add a user to the Prosody XMPP server:

`sudo prosodyctl adduser {{user@example.com}}`

- Set a user's password:

`sudo prosodyctl passwd {{user@example.com}}`

- Permanently delete a user:

`sudo prosodyctl deluser {{user@example.com}}`
