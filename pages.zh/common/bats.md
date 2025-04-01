# bats

> Bash 自动化测试系统：一个符合 TAP (Test Anything Protocol) 标准的 Bash 测试框架。
> 更多信息：<https://bats-core.readthedocs.io/en/stable/usage.html>。

- 运行 BATS 测试脚本并以 TAP (Test Anything Protocol) 格式输出结果：

`bats {{[-t|--tap]}} {{path/to/test.bats}}`

- 计算测试脚本中的测试用例数量，而不实际运行测试：

`bats {{[-c|--count]}} {{path/to/test.bats}}`

- 递归运行 BATS 测试用例（文件扩展名为 `.bats`）：

`bats {{[-r|--recursive]}} {{path/to/directory}}`

- 以特定格式输出结果：

`bats {{[-F|--formatter]}} {{pretty|tap|tap13|junit}} {{path/to/test.bats}}`

- 向测试添加时间信息：

`bats {{[-T|--timing]}} {{path/to/test.bats}}`

- 并行运行指定数量的作业（需要安装 GNU `parallel`）：

`bats {{[-j|--jobs]}} {{number}} {{path/to/test.bats}}`
