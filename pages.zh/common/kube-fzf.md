# kube-fzf

> 用于命令行中对 Kubernetes Pods 进行模糊搜索的 Shell 命令。
> 有关相关命令，请参见 `kubectl`。
> 更多信息：<https://github.com/thecasualcoder/kube-fzf>.

- 获取 Pod 详细信息（来自当前命名空间）:

`findpod`

- 获取 Pod 详细信息（来自所有命名空间）:

`findpod -a`

- 描述 Pod:

`describepod`

- 跟踪 Pod 日志:

`tailpod`

- 在 Pod 的容器中执行命令:

`execpod {{shell_command}}`

- 将 Pod 端口转发:

`pfpod {{port_number}}`