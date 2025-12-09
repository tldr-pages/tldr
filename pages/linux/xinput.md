# xinput

> List available input devices, query information about a device and change input device settings.
> More information: <https://manned.org/xinput>.

- List all input devices:

`xinput list`

- Disable an input:

`xinput disable {{id}}`

- Enable an input:

`xinput enable {{id}}`

- Disconnect an input from its master:

`xinput float {{id}}`

- Reattach an input as slave to a master:

`xinput reattach {{id}} {{master_id}}`

- List settings of an input device:

`xinput list-props {{id}}`

- Change a setting of an input device:

`xinput set-prop {{id}} {{setting_id}} {{value}}`
