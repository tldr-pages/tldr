# 投骰子

> 投掷虚拟骰子。
> 更多信息：<https://manned.org/rolldice>。

- 投一个20面骰：

`rolldice d{{20}}`

- 投两个6面骰，并去掉最低的点数：

`rolldice {{2}}d{{6}}s{{1}}`

- 投两个20面骰，并添加一个修正值：

`rolldice {{2}}d{{20}}{{+5}}`

- 投两个20面骰：

`rolldice {{2}}xd{{20}}`