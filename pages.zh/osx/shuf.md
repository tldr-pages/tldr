# shuf

> 生成随机排列。
> 更多信息：<https://keith.github.io/xcode-man-pages/shuf.1.html>.

- 随机化文件中的行顺序并输出结果：

`shuf {{文件名}}`

- 只输出结果的前 5 条：

`shuf --head-count=5 {{路径/到/文件}}`

- 将结果输出写入另一个文件：

`shuf {{路径/到/输入文件}} --output {{路径/到/输出文件}}`

- 生成范围（1-10）内的随机数：

`shuf --input-range=1-10`
