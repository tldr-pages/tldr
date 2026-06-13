# syncthing

> Continuous bidirectional decentralised folder synchronisation tool.
> More information: <https://docs.syncthing.net/users/syncthing.html>.

- Start Syncthing:

`syncthing`

- Start Syncthing without opening a web browser:

`syncthing --no-browser`

- Change the home directory:

`syncthing --home {{path/to/directory}}`

- Run Syncthing with increased logging:

`syncthing --verbose`

- Pause all devices:

`syncthing cli config devices pause --all`

- Resume all devices:

`syncthing cli config devices resume --all`

- Change the address upon which the web interface listens:

`syncthing --gui-address {{ip_address:port|path/to/socket.sock}}`

- Set the log level for output:

`syncthing --log-level {{info|warning|error|debug}}`
