# xinput

> List available input devices, query information about a device, and change input device settings.
> More information: <https://manned.org/xinput>.

- List all input devices:

`xinput list`

- Disable an input:

`xinput disable {{device_id}}`

- Enable an input:

`xinput enable {{device_id}}`

- Disconnect an input from its master:

`xinput float {{device_id}}`

- Reattach an input as slave to a master:

`xinput reattach {{device_id}} {{master_id}}`

- List settings of an input device:

`xinput list-props {{device_id}}`

- Change a setting of an input device:

`xinput set-prop {{device_id}} {{setting_id}} {{value}}`
