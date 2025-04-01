# pulumi destroy

> 删除堆栈中的所有现有资源。
> 更多信息：<https://www.pulumi.com/docs/iac/cli/commands/pulumi_destroy/>。

- 删除当前堆栈中的所有资源：

`pulumi destroy`

- 删除特定堆栈中的所有资源：

`pulumi destroy --stack {{stack}}`

- 预览后自动批准并删除资源：

`pulumi destroy --yes`

- 不删除受保护的资源：

`pulumi destroy --exclude-protected`

- 在删除堆栈中的所有资源后，删除堆栈及其配置文件：

`pulumi destroy --remove`

- 即使遇到错误也继续删除资源：

`pulumi destroy --continue-on-error`