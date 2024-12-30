# tailscale 文件

> 在 Tailscale 网络上的连接设备之间发送文件。
> 目前不支持向同一 Tailscale 网络中其他用户拥有的设备发送文件。
> 更多信息：<https://tailscale.com/kb/1106/taildrop/>.

- 将文件发送到特定节点：

`sudo tailscale file cp {{path/to/file}} {{hostname|ip}}:`

- 将发送到当前节点的文件存储到特定目录：

`sudo tailscale file get {{path/to/directory}}`