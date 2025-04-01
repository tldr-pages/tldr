# kubectl wait

> 等待资源达到某种状态。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#wait>.

- 等待一个部署可用：

`kubectl wait --for=condition=available deployment/{{deployment_name}}`

- 等待具有特定 [l]abel 的所有 pod 准备就绪：

`kubectl wait --for=condition=ready pod {{[-l|--selector]}} {{label_key}}={{label_value}}`

- 等待一个 pod 被删除：

`kubectl wait --for=delete pod {{pod_name}}`

- 等待一个作业完成，超时时间为 120 秒（如果条件未在规定时间内满足，退出状态将为失败）：

`kubectl wait --for=condition=complete job/{{job_name}} --timeout 120s`
