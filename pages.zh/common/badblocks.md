# badblocks

> 搜索设备上的坏块。
> 更多信息：<https://manned.org/badblocks>。

- 搜索设备上的坏块：

`sudo badblocks {{/dev/sda}}`

- 搜索设备上的坏块并显示进度：

`sudo badblocks -s {{/dev/sda}}`

- 搜索设备上的坏块并将结果保存到文件：

`sudo badblocks -o {{badblocks.txt}} {{/dev/sda}}`

- 非破坏性读写测试：

`sudo badblocks -nsv {{/dev/sda}}`
