# pbmtoascii

> 将 PBM 图像转换为 ASCII 图形。
> 另见：`ppmtoascii`, `asciitopgm`, `ppmtoterm`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtoascii.html>。

- 读取 PBM 文件作为输入并生成 ASCII 输出：

`pbmtoascii {{path/to/input_file.pbm}}`

- 读取 PBM 文件作为输入并将 ASCII 输出保存到文件中：

`pbmtoascii {{path/to/input_file.pbm}} > {{path/to/output_file}}`

- 读取 PBM 文件作为输入，同时设置像素映射（默认为 1x2）：

`pbmtoascii -{{1x2|2x4}} {{path/to/input_file.pbm}}`

- 显示版本：

`pbmtoascii -version`
