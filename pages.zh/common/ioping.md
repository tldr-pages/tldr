# ioping

> 实时监控 I/O 延迟。
> 更多信息：<https://github.com/koct9i/ioping>.

- 使用默认值和当前目录显示磁盘 I/O 延迟：

`ioping .`

- 使用 10 次 1 兆字节的请求测量 /tmp 的延迟：

`ioping -c 10 -s 1M /tmp`

- 测量 `/dev/sdX` 的磁盘寻道速率：

`ioping -R {{/dev/sdX}}`

- 测量 `/dev/sdX` 的磁盘顺序读写速度：

`ioping -RL {{/dev/sdX}}`