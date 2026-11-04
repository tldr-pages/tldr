# sio

> A comprehensive Linux hardware information and real-time sensor monitoring tool.
> More information: <https://github.com/level1techs/siomon>.

- Open Siomon TUI:

`sio`

- Set custom polling interval:

`sio --interval {{milliseconds}}`

- Snapshot the current sensor values:

`sio sensors`

- Output report to filetype:

`sio {{[-f|--format]}} {{json|xml|html}}`

- Output specific hardware details:

`sio {{cpu|gpu|memory|storage|network|pci|pcie|audio|usb|battery|board}}`

- Open sio with root sensor access:

`sudo sio`
