# choco new

> 使用 Chocolatey 生成新的包规范文件。
> 更多信息：<https://chocolatey.org/docs/commands-new>.

- 创建一个新的包框架：

`choco new {{包名}}`

- 创建一个新的指定版本的包：

`choco new {{包名}} --version {{版本号}}`

- 创建一个新的包并指定维护者的名字：

`choco new {{包名}} --maintainer {{维护者名字}}`

- 在指定目录下创建新的包：

`choco new {{包名}} --output-directory {{指定的目录路径}}`

- 创建一个新的包并指定其 32 位版和 64 位版的安装 URL：

`choco new {{package_name}} url="{{url}}" url64="{{url}}"`
