# frida-ps

> List processes on a local or remote device.
> More information: <https://frida.re/docs/frida-ps/>.

- List all running processes on the local machine:

`frida-ps`

- List all running processes on a USB-connected device:

`frida-ps {{[-U|--usb]}}

- List all running applications on a USB-connected device:

`frida-ps {{[-U|--usb]}} {{[-a|--applications]}}`

- List all installed applications on a USB-connected device:

`frida-ps {{[-U|--usb]}} {{[-i|--installed]}}`

- List processes on a specific device:

`frida-ps {{[-D|--device]}} {{device_id}}`
