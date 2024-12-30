# tmt 运行

> 执行 tmt 测试步骤。默认情况下，所有步骤都会运行。
> 更多信息：<https://tmt.readthedocs.io/en/stable/overview.html#run>。

- 为每个计划运行所有测试步骤：

`tmt run`

- 仅运行发现步骤，以显示将要运行的测试：

`tmt run discover -v`

- 运行所有步骤并调整供应步骤选项：

`tmt run --all provision --how {{container}} --image {{fedora:rawhide}}`

- 仅运行选定的计划和测试：

`tmt run plan --name {{/plan/name}} test --name {{/test/name}}`

- 在网页浏览器中显示上次运行的结果：

`tmt run --last report --how {{html}} --open`

- 使用提供的上下文运行测试：

`tmt run --context {{key=value}} -c {{distro=fedora}}`

- 交互式运行测试（在测试过程中调试测试代码）：

`tmt run --all execute --how {{tmt}} --interactive`

- 使用干运行模式查看将会发生的操作，并使用最高的详细程度：

`tmt run --dry -vvv`