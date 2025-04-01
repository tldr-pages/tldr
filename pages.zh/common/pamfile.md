# pamfile

> 描述 Netpbm (PAM 或 PNM) 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamfile.html>.

- 描述指定的 Netpbm 文件：

`pamfile {{path/to/file1 path/to/file2 ...}}`

- 以机器可读格式描述每个输入文件中的所有图像（而不仅仅是每个文件中的第一个图像）：

`pamfile -allimages -machine {{path/to/file}}`

- 显示输入文件包含的图像数量：

`pamfile -count {{path/to/file}}`