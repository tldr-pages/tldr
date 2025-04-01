# obabel

> 转换化学相关数据。
> 更多信息：<https://open-babel.readthedocs.io/en/latest/Command-line_tools/babel.html>。

- 将 .mol 文件转换为 XYZ 坐标：

`obabel {{path/to/file.mol}} -O {{path/to/output_file.xyz}}`

- 将 SMILES 字符串转换为 500x500 的图片：

`obabel -:"{{SMILES}}" -O {{path/to/output_file.png}} -xp 500`

- 将包含 SMILES 字符串的文件转换为多个 3D .mol 文件：

`obabel {{path/to/file.smi}} -O {{path/to/output_file.mol}} --gen3D -m`

- 将多个输入渲染为一张图片：

`obabel {{path/to/file1 path/to/file2 ...}} -O {{path/to/output_file.png}}`
