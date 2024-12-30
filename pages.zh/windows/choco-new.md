# choco new

> 使用 Chocolatey 生成新的包规范文件。
> 更多信息：<https://chocolatey.org/docs/commands-new>。

- 创建一个新的包骨架：

`choco new {{package}}`

- 创建一个具有特定版本的新包：

`choco new {{package}} --version {{version}}`

- 创建一个具有特定维护者名称的新包：

`choco new {{package}} --maintainer {{maintainer_name}}`

- 在自定义输出目录中创建一个新包：

`choco new {{package}} --output-directory {{path/to/directory}}`

- 创建一个具有特定 32 位和 64 位安装程序 URL 的新包：

`choco new {{package}} url="{{url}}" url64="{{url}}"`