# shuf

> 生成随机排列。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/shuf-invocation.html>。

- 随机排列文件中的行并输出结果：

`shuf {{路径/到/文件}}`

- 仅输出结果的前 5 行：

`shuf {{[-n|--head-count]}} 5 {{路径/到/文件}}`

- 将输出写入另一个文件：

`shuf {{路径/到/输入文件}} {{[-o|--output]}} {{路径/到/输出文件}}`

- 生成 3 个 1-10 范围内的随机数（含，数字可重复）：

`shuf {{[-n|--head-count]}} 3 {{[-i|--input-range]}} 1-10 {{[-r|--repeat]}}`
