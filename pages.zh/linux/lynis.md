# lynis

> 系统和安全审计工具。
> 更多信息：<https://cisofy.com/documentation/lynis/>。

- 检查 Lynis 是否是最新的：

`sudo lynis update info`

- 运行系统的安全审计：

`sudo lynis audit system`

- 运行 Dockerfile 的安全审计：

`sudo lynis audit dockerfile {{path/to/dockerfile}}`