# choco new

> 使用 Chocolatey 生成新的包规范文件。
> 更多信息：<https://docs.chocolatey.org/en-us/create/commands/new/>。

- 创建一个新的包框架：

`choco new {{软件包}}`

- 创建一个新的指定版本的包：

`choco new {{软件包}} --version {{版本号}}`

- 创建一个新的包并指定维护者的名字：

`choco new {{软件包}} --maintainer {{维护者名字}}`

- 在指定目录下创建新的包：

`choco new {{软件包}} {{[--out|--output-directory]}} {{指定的目录路径}}`

- 创建一个新的包并指定其 32 位版和 64 位版的安装 URL：

`choco new {{软件包}} url="{{url}}" url64="{{url}}"`
