# xinput

> List available input devices, query information about a device and change input device settings.

- List all input devices:

`xinput list`

- Disconnect an input from its master:

`xinput float {{id}}`

- Reattach an input as slave to a master:

`xinput reattach {{id}} {{master_id}}`
