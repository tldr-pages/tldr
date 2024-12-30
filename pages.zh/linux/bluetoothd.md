# bluetoothd

> 用于管理蓝牙设备的守护进程。
> 更多信息：<https://manned.org/bluetoothd>。

- 启动守护进程：

`bluetoothd`

- 启动守护进程，日志输出到 `stdout`：

`bluetoothd --nodetach`

- 使用特定配置文件启动守护进程（默认为 `/etc/bluetooth/main.conf`）：

`bluetoothd --configfile {{path/to/file}}`

- 启动守护进程，并将详细输出发送到 `stderr`：

`bluetoothd --debug`

- 启动守护进程，详细输出来自 bluetoothd 或插件源中的特定文件：

`bluetoothd --debug={{path/to/file1:path/to/file2:...}}`