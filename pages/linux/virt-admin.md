# virt-admin

> Manage and monitor the libvirt daemon, including connected clients, server settings, logging, and daemon behaviour.
> More information: <https://manned.org/virt-admin>.

- Start the interactive administration shell:

`virt-admin`

- Connect to a specific daemon and print the version:

`virt-admin {{[-c|--connect]}} {{virtqemud:///system}} version`

- Dispplay information about a specific connected client:

`virt-admin client-info {{server}} {{client_id}}`

- Shut down the libvirt daemon gracefully:

`virt-admin daemon-shutdown`

- Shut down the daemon while preserving running virtual machines:

`virt-admin daemon-shutdown --preserve`

- Display available commands:

`virt-admin help`
