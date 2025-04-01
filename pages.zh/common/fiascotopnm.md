# fiascotopnm

> 将压缩的 FIASCO 文件转换为 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/fiascotopnm.html>。

- 将压缩的 FIASCO 文件转换为 PNM 文件，或在处理视频流时生成多个 PNM 文件：

`fiascotopnm {{path/to/file.fiasco}} -o {{output_file_basename}}`

- 使用快速解压缩，导致输出文件质量略有下降：

`fiascotopnm --fast {{path/to/file.fiasco}} -o {{output_file_basename}}`

- 从指定的配置文件中加载要使用的选项：

`fiascotopnm --config {{path/to/fiascorc}} {{path/to/file.fiasco}} -o {{output_file_basename}}`

- 将解压缩的图像放大 2^n 倍：

`fiascotopnm --magnify {{n}} {{path/to/file.fiasco}} -o {{output_file_basename}}`

- 通过指定的量平滑解压缩的图像：

`fiascotopnm --smooth {{n}} {{path/to/file.fiasco}} -o {{output_file_basename}}`