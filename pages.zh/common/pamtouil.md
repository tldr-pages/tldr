# pamtouil

> 将 PNM 或 PAM 文件转换为 Motif UIL 图标文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamtouil.html>。

- 将 PNM 或 PAM 文件转换为 Motif UIL 图标文件：

`pamtouil {{path/to/input.pnm|pam}} > {{path/to/output.uil}}`

- 指定一个前缀字符串以在输出 UIL 文件中打印：

`pamtouil -name {{uilname}} {{path/to/input.pnm|pam}} > {{path/to/output.uil}}`