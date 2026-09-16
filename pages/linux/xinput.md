# xinput

> List available input devices, query information about a device and change input device settings.
> More information: <https://manned.org/xinput>.

- List all input devices:

`xinput list`

- Disable an input:

`xinput disable {{input_device_id}}`

- Enable an input:

`xinput enable {{input_device_id}}`

- Disconnect an input from its master:

`xinput float {{input_device_id}}`

- Reattach an input as slave to a master:

`xinput reattach {{input_device_id}} {{master_id}}`

- List settings of an input device:

`xinput list-props {{input_device_id}}`

- Change a setting of an input device:

`xinput set-prop {{input_device_id}} {{setting_id}} {{value}}`
