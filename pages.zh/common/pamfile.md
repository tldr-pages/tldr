# pamfile

> 描述 Netpbm (PAM 或 PNM) 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamfile.html>。

- 描述指定的 Netpbm 文件：

`pamfile {{路径/到/文件1 路径/到/文件2 ...}}`

- 以机器可读格式描述每个输入文件中的每个图像（与仅描述每个文件中的第一个图像相对）：

`pamfile -allimages -machine {{路径/到/文件}}`

- 显示输入文件包含多少个图像的计数：

`pamfile -count {{路径/到/文件}}`