# stl2gts

> 将 STL 文件转换为 GTS (GNU 三角形表面库) 文件格式。
> 更多信息：<https://manned.org/stl2gts>.

- 将 STL 文件转换为 GTS 文件：

`stl2gts < {{path/to/file.stl}} > {{path/to/file.gts}}`

- 将 STL 文件转换为 GTS 文件并反转面法线：

`stl2gts --revert < {{path/to/file.stl}} > {{path/to/file.gts}}`

- 将 STL 文件转换为 GTS 文件且不合并顶点：

`stl2gts --nomerge < {{path/to/file.stl}} > {{path/to/file.gts}}`

- 将 STL 文件转换为 GTS 文件并显示表面统计信息：

`stl2gts --verbose < {{path/to/file.stl}} > {{path/to/file.gts}}`

- 显示帮助：

`stl2gts --help`