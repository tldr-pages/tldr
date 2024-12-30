# kube-capacity

> 提供Kubernetes集群中资源请求、限制和利用率的概述。
> 将`kubectl top`和`kubectl describe`的最佳部分结合成一个专注于集群资源的CLI。
> 更多信息：<https://github.com/robscott/kube-capacity>。

- 列出节点，包括总CPU和内存资源请求和限制：

`kube-capacity`

- 包括Pods：

`kube-capacity -p`

- 包括利用率：

`kube-capacity -u`