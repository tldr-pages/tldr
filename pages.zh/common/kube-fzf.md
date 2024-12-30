# kube-fzf

> 用于对Kubernetes Pods进行命令行模糊搜索的Shell命令。
> 另请参见与之相关的命令`kubectl`。
> 更多信息：<https://github.com/thecasualcoder/kube-fzf>。

- 获取Pod详细信息（来自当前命名空间）：

`findpod`

- 获取Pod详细信息（来自所有命名空间）：

`findpod -a`

- 描述一个Pod：

`describepod`

- 尾随Pod日志：

`tailpod`

- 进入Pod的容器：

`execpod {{shell_command}}`

- 端口转发到Pod：

`pfpod {{port_number}}`