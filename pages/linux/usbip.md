# usbip

> Tool for using USB devices remotely
> More information: <https://usbip.sourceforge.net/>.

- List all local USB devices and they busid's:

`usbip list --local`

- Start the usbip daemon on the server:

`systemctl start usbipd`

- Bind a USB device to usbip on the server:

`sudo usbip bind -b {{busid}}`

- Load the kernel module required by usbip on the client:

`sudo modprobe vhci-hcd`

- Attach to the usbip device on the client (busid is the same as on the server):

`sudo usbip attach -r {{ip_address}} -b {{busid}}`
