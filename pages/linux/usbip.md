# usbip

> Use USB devices remotely.
> More information: <https://usbip.sourceforge.net>.

- List all local USB devices and their bus ID's:

`usbip list --local`

- Start a `usbip` daemon on the server:

`systemctl start usbipd`

- Bind a USB device to `usbip` on the server:

`sudo usbip bind --busid={{bus_id}}`

- Load the kernel module required by `usbip` on the client:

`sudo modprobe vhci-hcd`

- Attach to the `usbip` device on the client (bus ID is the same as on the server):

`sudo usbip attach -r {{ip_address}} --busid={{bus_id}}`

- List attached devices:

`usbip port`

- Detach from a device:

`sudo usbip detach --port={{port}}`

- Unbind a device:

`usbip unbind --busid={{bus_id}}`
