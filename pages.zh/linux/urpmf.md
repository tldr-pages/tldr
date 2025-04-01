# urpmf

> 在 Mageia 中查找软件包中的文件并查询相关信息。
> 参见：`urpmi`，`urpme`，`urpmi.addmedia`，`urpmi.removemedia`，`urpmi.update`，`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpmf>。

- 搜索包含指定文件的软件包：

`urpmf {{filename}}`

- 搜索在摘要中同时包含两个关键字的软件包：

`urpmf --summary {{keyword1}} -a {{keyword2}}`

- 搜索在描述中包含任一关键字的软件包：

`urpmf --description {{keyword1}} -o {{keyword2}}`

- 搜索名称中不包含指定关键字的软件包，忽略大小写，使用 "|" 作为字段分隔符（默认为 ":"）：

`urpmf --description ! {{keyword}} -F'|'`
