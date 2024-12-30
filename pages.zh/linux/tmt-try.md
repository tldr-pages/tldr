# tmt 尝试

> 快速实验测试和环境。
> 更多信息：<https://tmt.readthedocs.io/en/stable/stories/cli.html#try>。

- 快速实验默认的提供方法（当前工作目录中没有测试）：

`tmt try`

- 在当前工作目录中运行测试：

`cd {{path/to/test}} && tmt try`

- 使用特定的操作系统：

`tmt try {{fedora-41}}`

- 选择自定义镜像和提供方法：

`tmt try {{fedora@container}}`

- 使用自定义过滤器选择测试：

`tmt try --test {{feature}}`

- 提供来宾并等待指示：

`tmt try --ask`

- 直接登录到来宾而不询问：

`tmt try --login`

- 显示帮助信息：

`tmt try --help`