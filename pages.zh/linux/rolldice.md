# rolldice

> 滚动虚拟骰子。
> 更多信息：<https://manned.org/rolldice>.

- 滚动一个20面的骰子：

`rolldice d{{20}}`

- 滚动两个6面的骰子并丢弃最低的一次结果：

`rolldice {{2}}d{{6}}s{{1}}`

- 滚动两个20面的骰子并加上一个修正值：

`rolldice {{2}}d{{20}}{{+5}}`

- 滚动一个20面的骰子两次：

`rolldice {{2}}xd{{20}}`