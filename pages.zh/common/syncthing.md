# syncthing

> 持续的双向去中心化文件夹同步工具。
> 更多信息：<https://docs.syncthing.net/>.

- 启动 Syncthing:

`syncthing`

- 启动 Syncthing 但不打开网页浏览器:

`syncthing -no-browser`

- 打印设备 ID:

`syncthing -device-id`

- 更改主目录:

`syncthing -home={{path/to/directory}}`

- 强制进行完整的索引交换:

`syncthing -reset-deltas`

- 更改网页界面监听的地址:

`syncthing -gui-address={{ip_address:port|path/to/socket.sock}}`

- 显示 Syncthing 使用的文件路径:

`syncthing -paths`

- 禁用 Syncthing 监控进程:

`syncthing -no-restart`