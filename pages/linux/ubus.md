# ubus

> Interact with an OpenWrt ubusd server.
> More information: <https://openwrt.org/docs/techref/ubus>.

- List available objects:

`ubus list`

- Retrieve system information in JSON format:

`ubus call system board`

- Listen to events:

`ubus subscribe {{event_name}}`

- Display help:

`ubus`
