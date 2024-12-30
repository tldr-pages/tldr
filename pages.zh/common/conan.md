# conan

> 开源的、去中心化的跨平台包管理器，用于创建和共享所有本地二进制文件。
> 一些子命令，如 `frogarian`，有其自己的使用文档。
> 更多信息请访问: <https://conan.io/>。

- 根据 `conanfile.txt` 安装包：

`conan install {{.}}`

- 安装包并为特定生成器创建配置文件：

`conan install -g {{generator}}`

- 从源代码构建并安装包：

`conan install {{.}} --build`

- 搜索本地已安装的包：

`conan search {{package}}`

- 搜索远程包：

`conan search {{package}} -r {{remote}}`

- 列出远程源：

`conan remote list`