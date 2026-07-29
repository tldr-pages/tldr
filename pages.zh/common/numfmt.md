# numfmt

> 在数字和人类可读的字符串之间转换。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>。

- 将 1.5K（SI 单位）转换为 1500：

`numfmt --from si 1.5K`

- 将 1500 转换为 1.5K（SI 单位）：

`numfmt --to si 1500`

- 将 1.5K（IEC 单位）转换为 1536：

`numfmt --from iec 1.5K`

- 根据后缀使用适当的转换：

`numfmt --from auto {{1.5Ki}}`

- 将第 5 个字段（从 1 开始计数）转换为 IEC 单位，不转换表头：

`ls -l | numfmt --header=1 --field 5 --to iec`

- 转换为 IEC 单位，左对齐填充 5 个字符：

`du {{[-s|--summarize]}} * | numfmt --to iec --format "%-5f"`
