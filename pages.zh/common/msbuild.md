# msbuild

> Microsoft 为 Visual Studio 项目解决方案提供的构建工具。
> 更多信息：<https://learn.microsoft.com/visualstudio/msbuild>.

- 构建当前目录中的第一个项目文件：

`msbuild`

- 构建特定的项目文件：

`msbuild {{path/to/project_file}}`

- 指定一个或多个以分号分隔的构建目标：

`msbuild {{path/to/project_file}} /target:{{targets}}`

- 指定一个或多个以分号分隔的属性：

`msbuild {{path/to/project_file}} /property:{{name=value}}`

- 指定要使用的构建工具版本：

`msbuild {{path/to/project_file}} /toolsversion:{{version}}`

- 在日志末尾显示关于项目配置的详细信息：

`msbuild {{path/to/project_file}} /detailedsummary`

- 显示帮助：

`msbuild /help`
