# brew services

> Manage background services with `launchctl` on macOS or `systemctl` on Linux.
> More information: <https://docs.brew.sh/Manpage#services-subcommand>.

- List all managed services for the current user:

`brew services`

- List more information about all managed services:

`brew services info --all`

- Start a service immediately and register it to launch at login (or boot):

`brew services start {{formula}}`

- Stop the service immediately and unregister it from launching at login (or boot):

`brew services stop {{formula}}`

- Stop (if necessary) and start the service immediately and register it to launch at login (or boot):

`brew services restart {{formula}}`

- Remove all unused services:

`brew services cleanup`
