# tmt try

> 测试及环境快速上手。
> 更多信息：<https://tmt.readthedocs.io/en/stable/stories/cli.html#try>.

- 快速尝试默认的测试环境配置方法（当前工作目录中没有测试）：

`tmt try`

- 在当前的工作目录中运行一个测试：

`cd {{path/to/test}} && tmt try`

- 使用特定的操作系统：

`tmt try {{fedora-41}}`

- 选择定制的镜像和测试环境配置方法：

`tmt try {{fedora@container}}`

- 根据定制的筛选条件选择测试：

`tmt try --test {{feature}}`

- 配置客户机并等待用户输入指令：

`tmt try --ask`

- 直接登录到客户机：

`tmt try --login`

- 显示帮助：

`tmt try --help`
