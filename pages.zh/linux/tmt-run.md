# tmt run

> 执行测试步骤。默认情况下，所有测试步骤都被执行。
> 更多信息：<https://tmt.readthedocs.io/en/stable/stories/cli.html#run>.

- 在每一个计划中执行所有测试步骤：

`tmt run`

- 仅在发现步骤中显示将要执行的测试：

`tmt run discover -v`

- 运行所有测试步骤并调整测试环境配置步骤选项：

`tmt run --all provision --how {{container}} --image {{fedora:rawhide}}`

- 仅执行选定的计划和测试：

`tmt run plan --name {{/plan/name}} test --name {{/test/name}}`

- 在网页浏览器中显示上次运行的结果：

`tmt run --last report --how {{html}} --open`

- 在提供的上下文中运行测试：

`tmt run --context {{key=value}} -c {{distro=fedora}}`

- 以交互方式运行测试（在测试运行过程中调试测试代码）：

`tmt run --all execute --how {{tmt}} --interactive`

- 使用干模式查看接下来将发生的动作，并将输出详实度设置为最高级：

`tmt run --dry -vvv`
