# numfmt

> 将数字在人类可读的字符串和普通数字之间进行转换。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>.

- 将 1.5K (SI 单位) 转换为 1500：

`numfmt --from si 1.5K`

- 将第 5 列（从 1 开始计数）转换为 IEC 单位，不转换标题行：

`ls -l | numfmt --header=1 --field 5 --to iec`

- 转换为 IEC 单位，用 5 个字符左对齐填充：

`du {{[-s|--summarize]}} * | numfmt --to iec --format "%-5f"`
