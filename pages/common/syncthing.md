# syncthing

> Continuous bidirectional decentralised folder synchronisation tool.
> More information: <https://docs.syncthing.net/users/syncthing.html>.

- Print the device ID:

`syncthing --device-id`

- Change the home directory:

`syncthing --home {{path/to/directory}}`

- Force a full index exchange in order to resolve out of sync files:

`syncthing --reset-deltas`

- Change the address upon which the web interface listens:

`syncthing --gui-address {{ip_address:port|path/to/socket.sock}}`

- Show filepaths to the files used by Syncthing:

`syncthing --paths`

- Disable the Syncthing monitor process:

`syncthing --no-restart`

- Set the log level for output:

`syncthing --log-level {{info|warning|error|debug}}`

- Configure retention time for deleted items in the database:

`syncthing --db-delete-retention-interval {{duration}}`
