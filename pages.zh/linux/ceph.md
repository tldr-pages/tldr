# ceph

> 一个统一的存储系统。
> 更多信息：<https://ceph.io/en>。

- 检查集群健康状态：

`ceph status`

- 检查集群使用统计：

`ceph df`

- 获取集群中放置组的统计信息：

`ceph pg dump --format {{plain}}`

- 创建一个存储池：

`ceph osd pool create {{pool_name}} {{page_number}}`

- 删除一个存储池：

`ceph osd pool delete {{pool_name}}`

- 重命名一个存储池：

`ceph osd pool rename {{current_name}} {{new_name}}`

- 自我修复池存储：

`ceph pg repair {{pool_name}}`