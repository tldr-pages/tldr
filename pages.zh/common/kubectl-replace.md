# kubectl replace

> 通过文件或 `stdin` 替换资源。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#replace>.

- 使用资源定义文件替换资源：

`kubectl replace -f {{path/to/file.yml}}`

- 使用通过 `stdin` 输入的内容替换资源：

`kubectl replace -f -`

- 强制替换，先删除再重新创建资源：

`kubectl replace --force -f {{path/to/file.yml}}`
