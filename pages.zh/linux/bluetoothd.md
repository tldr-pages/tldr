# bluetoothd

> 管理蓝牙设备的守护进程。
> 更多信息：<https://manned.org/bluetoothd>.

- 启动守护进程：

`bluetoothd`

- 启动守护进程，日志输出到标准输出：

`bluetoothd --nodetach`

- 指定一个配置文件启动守护进程（默认是 `/etc/bluetooth/main.conf`）：

`bluetoothd --configfile {{配置文件}}`

- 启动守护进程并将详细信息输出到标准错误：

`bluetoothd --debug`

- 使用来自 bluetoothd 或插件源中特定文件启动守护进程并输出详细信息：

`bluetoothd --debug={{文件一}}:{{文件二}}:{{文件三}}`
