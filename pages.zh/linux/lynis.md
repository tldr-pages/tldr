# lynis

> 系统和安全审计工具。
> 更多信息：<https://cisofy.com/documentation/lynis/>.

- 检查 Lynis 是否为最新版本：

`sudo lynis update info`

- 运行系统的安全审计：

`sudo lynis audit system`

- 审计 Dockerfile 的安全性：

`sudo lynis audit dockerfile {{path/to/dockerfile}}`
