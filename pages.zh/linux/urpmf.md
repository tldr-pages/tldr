# urpmf

> 在Mageia中查找包中的文件并查询有关它们的信息。
> 另见：`urpmi`，`urpme`，`urpmi.addmedia`，`urpmi.removemedia`，`urpmi.update`，`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpmi.removemedia>。

- 查找包含文件的包：

`urpmf {{filename}}`

- 查找在摘要中同时包含两个关键字的包：

`urpmf --summary {{keyword1}} -a {{keyword2}}`

- 查找在描述中包含一个关键字或另一个的包：

`urpmf --description {{keyword1}} -o {{keyword2}}`

- 查找名称中不包含关键字的包，忽略大小写，使用"|"作为字段分隔符（默认是":"）：

`urpmf --description ! {{keyword}} -F'|'`