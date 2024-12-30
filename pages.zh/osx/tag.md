# 标签

> 在 Mac OS X 文件上编辑标签（10.9 Mavericks 及以上版本）。
> 更多信息：<https://github.com/jdberry/tag/>。

- 向文件添加标签：

`tag --add {{标签名称1,标签名称2,...}} {{文件路径}}`

- 移除一个标签：

`tag --remove {{标签名称}} {{文件路径}}`

- 从文件中移除所有标签：

`tag --remove \* {{文件路径}}`

- 显示所有具有给定标签的文件：

`tag --match {{标签名称}}`