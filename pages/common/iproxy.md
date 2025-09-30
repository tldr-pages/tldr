# iproxy

> A proxy that binds local TCP ports to be forwarded to the specified ports on a usbmux device.
> More information: <https://manned.org/iproxy>.

- Bind a local TCP port and forward it to a port on the connected USB device:

`iproxy {{local_port}}:{{device_port}}`

- Bind multiple local TCP ports and forward them to the respective ports on the connected USB device:

`iproxy {{local_port1}}:{{device_port1}} {{local_port2}}:{{device_port2}}`

- Bind a local port and forward it to a specific device by UDID:

`iproxy --udid {{device_udid}} {{local_port}}:{{device_port}}`

- Bind a local port and forward it to a network-connected device with WiFi sync enabled:

`iproxy --network {{local_port}}:{{device_port}}`
