# tailscale file

> 在 Tailscale 网络中发送文件到已连接的设备。
> 目前不支持发送文件到同一 Tailscale 网络中其他用户拥有的设备。
> 更多信息：<https://tailscale.com/kb/1106/taildrop/>.

- 向特定节点发送文件：

`tailscale file cp {{path/to/file}} {{hostname|ip}}:`

- 将发送到当前节点的文件存储到特定目录中：

`tailscale file get {{path/to/directory}}`