# sio

> A comprehensive Linux hardware information and real-time sensor monitoring tool.
> More information: <https://github.com/level1techs/siomon>.

- Open Siomon TUI:

`sio`

- Custom polling interval TUI:

`sio --interval {{milliseconds}}`

- Snapshot of current sensor values:

`sio sensors`

- Output report to filetype:

`sio -f {{json|xml|html|}}`

- Output specific hardware details:

`sio {{cpu|gpu|memory|storage|network|pci|pcie|audio|usb|battery|board}}`

- Root sensor access:

`sudo sio`
