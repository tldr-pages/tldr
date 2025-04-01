# conan

> 开源、分散式、跨平台的包管理器，用于创建和分享所有的本地二进制文件。
> 一些子命令如 `frogarian` 有它们自己的使用文档。
> 更多信息：<https://conan.io/>。

- 基于 `conanfile.txt` 安装包：

`conan install {{.}}`

- 安装包并为指定的生成器创建配置文件：

`conan install -g {{generator}}`

- 安装包，从源代码构建：

`conan install {{.}} --build`

- 搜索本地已安装的包：

`conan search {{package}}`

- 搜索远程包：

`conan search {{package}} -r {{remote}}`

- 列出远程源：

`conan remote list`