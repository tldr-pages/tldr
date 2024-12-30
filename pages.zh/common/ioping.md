# ioping

> 实时监控I/O延迟。
> 更多信息：<https://github.com/koct9i/ioping>。

- 使用默认值和当前目录显示磁盘I/O延迟：

`ioping .`

- 在/tmp上使用10个每个1兆字节的请求测量延迟：

`ioping -c 10 -s 1M /tmp`

- 测量`/dev/sdX`上的磁盘寻道速率：

`ioping -R {{/dev/sdX}}`

- 测量`/dev/sdX`上的磁盘顺序速度：

`ioping -RL {{/dev/sdX}}`