# assimp

> Open Asset Import Library 的客户端。
> 支持加载 40 多种 3D 文件格式，并可导出为多种常用的 3D 格式。
> 更多信息：<https://manned.org/assimp>.

- 列出所有支持的导入格式：

`assimp listext`

- 列出所有支持的导出格式：

`assimp listexport`

- 使用默认参数将文件转换为支持的输出格式之一：

`assimp export {{输入文件.stl}} {{输出文件.obj}}`

- 使用自定义参数转换文件（assimp 源代码中的 dox_cmd.h 文件列出了可用参数）：

`assimp export {{输入文件.stl}} {{输出文件.obj}} {{参数}}`

- 显示 3D 文件内容的概要信息：

`assimp info {{路径/到/文件}}`

- 显示帮助信息：

`assimp help`

- 显示特定子命令的帮助信息：

`assimp {{子命令}} --help`
