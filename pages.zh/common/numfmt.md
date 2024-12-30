# numfmt

> 将数字转换为人类可读的字符串，反之亦然。
> 更多信息：<https://www.gnu.org/software/coreutils/numfmt>。

- 将 1.5K（国际单位制）转换为 1500：

`numfmt --from=si 1.5K`

- 将第 5 列（1 索引）转换为 IEC 单位，不转换表头：

`ls -l | numfmt --header=1 --field=5 --to=iec`

- 转换为 IEC 单位，填充 5 个字符，左对齐：

`du -s * | numfmt --to=iec --format="%-5f"`