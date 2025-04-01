# xvfb-run

> 在虚拟 X 服务器环境中运行命令。
> 更多信息：<https://www.x.org/wiki/>.

- 在虚拟 X 服务器中运行指定的命令：

`xvfb-run {{command}}`

- 如果默认服务器编号（99）不可用，尝试获取一个空闲的服务器编号：

`xvfb-run --auto-servernum {{command}}`

- 传递参数给 Xvfb 服务器：

`xvfb-run --server-args "{{-screen 0 1024x768x24}}" {{command}}`
