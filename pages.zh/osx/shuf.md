# shuf

> 生成随机排列。
> 更多信息：<https://keith.github.io/xcode-man-pages/shuf.1.html>。

- 随机化文件中行的顺序并输出结果：

`shuf {{路径/到/文件}}`

- 仅输出结果的前 5 个条目：

`shuf --head-count=5 {{路径/到/文件}}`

- 将输出写入另一个文件：

`shuf {{路径/到/输入文件}} --output={{路径/到/输出文件}}`

- 生成范围为 1 到 10 的随机数字：

`shuf --input-range=1-10`