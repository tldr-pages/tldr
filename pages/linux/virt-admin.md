# virt-admin

> Manage and monitor the libvirt daemon, including connected clients, server settings, logging, and daemon behaviour.
> More information: <https://manned.org/virt-admin>.

- Start the interactive administration shell:

`virt-admin`

- Connect to a specific daemon and print the version:

`virt-admin {{[-c|--connect]}} {{virtqemud:///system}} version`

- Dispplay information about a specific connected client:

`virt-admin client-info {{server}} {{client_id}}`

- Instruct the daemon to exit gracefully:

`virt-admin daemon-shutdown`

- Display available commands:

`virt-admin help`
