# assimp

> 开放资产导入库的命令行客户端。
> 支持加载40多种3D文件格式，并导出为几种流行的3D格式。
> 更多信息：<https://assimp-docs.readthedocs.io/>.

- 列出所有支持的导入格式：

`assimp listext`

- 列出所有支持的导出格式：

`assimp listexport`

- 将文件转换为支持的输出格式之一，使用默认参数：

`assimp export {{input_file.stl}} {{output_file.obj}}`

- 使用自定义参数转换文件（assimp源代码中的dox_cmd.h文件列出了可用参数）：

`assimp export {{input_file.stl}} {{output_file.obj}} {{parameters}}`

- 显示3D文件内容的摘要：

`assimp info {{path/to/file}}`

- 显示帮助：

`assimp help`

- 显示特定子命令的帮助：

`assimp {{subcommand}} --help`