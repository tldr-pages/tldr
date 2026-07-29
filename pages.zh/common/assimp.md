# assimp

> Open Asset Import Library 的客户端。
> 支持加载 40+ 种 3D 文件格式，并导出为几种流行的 3D 格式。
> 更多信息：<https://manned.org/assimp>。

- 列出所有支持的导入格式：

`assimp listext`

- 列出所有支持的导出格式：

`assimp listexport`

- 使用默认参数将文件转换为支持的输出格式之一：

`assimp export {{input_file.stl}} {{output_file.obj}}`

- 使用自定义参数转换文件（assimp 源代码中的 dox_cmd.h 文件列出了可用参数）：

`assimp export {{input_file.stl}} {{output_file.obj}} {{参数}}`

- 显示 3D 文件内容的摘要：

`assimp info {{路径/到/文件}}`

- 显示帮助：

`assimp help`

- 显示特定子命令的帮助：

`assimp {{子命令}} --help`
