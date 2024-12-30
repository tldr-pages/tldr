# delpart

> 请求Linux内核忘记一个分区。
> 更多信息：<https://manned.org/delpart>。

- 告诉内核忘记`/dev/sda`的第一个分区：

`sudo delpart {{/dev/sda}} {{1}}`