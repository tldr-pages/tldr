# switcherooctl

> Launch a command on a specific GPU.
> More information: <https://manned.org/switcherooctl>.

- Enable the switcheroo service:

`systemctl start switcheroo-control`

- List known GPUs:

`switcherooctl`

- Launch a command on the first discrete GPU:

`switcherooctl launch {{command}}`

- Launch a command on a specific GPU:

`switcherooctl launch {{[-g|--gpu]}} {{device_number}} {{command}}`

- Display help:

`switcherooctl help`
