# ahost

> DNS查找工具，用于显示与主机名或IP地址相关联的A或AAAA记录。
> 更多信息：<https://manned.org/ahost>。

- 打印与主机名或IP地址相关联的`A`或`AAAA`记录：

`ahost {{example.com}}`

- 显示一些额外的调试输出：

`ahost -d {{example.com}}`

- 显示指定类型的记录：

`ahost -t {{a|aaaa|u}} {{example.com}}`