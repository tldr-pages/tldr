# frida-ps

> List processes on a local or remote device.
> More information: <https://frida.re/docs/frida-ps/>.

- List all running processes on the local machine:

`frida-ps`

- List all running processes on a USB-connected device:

`frida-ps --usb`

- List all running applications on a USB-connected device:

`frida-ps --usb --applications`

- List all installed applications on a USB-connected device:

`frida-ps --usb --installed`

- List processes on a specific device:

`frida-ps --device {{device_id}}`
