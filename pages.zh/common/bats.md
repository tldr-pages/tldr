# bats

> Bash 自动化测试系统：一个符合 TAP (<https://testanything.org/>) 的 Bash 测试框架。
> 更多信息：<https://bats-core.readthedocs.io/en/stable/usage.html>。

- 运行 BATS 测试脚本并以 [t]AP（测试任何协议）格式输出结果：

`bats --tap {{path/to/test.bats}}`

- 计算测试脚本中的测试用例数量而不运行任何测试：

`bats --count {{path/to/test.bats}}`

- 递归运行 BATS 测试用例（文件扩展名为 `.bats` 的文件）：

`bats --recursive {{path/to/directory}}`

- 以特定 [F]ormat 输出结果：

`bats --formatter {{pretty|tap|tap13|junit}} {{path/to/test.bats}}`

- 向测试添加 [T]iming 信息：

`bats --timing {{path/to/test.bats}}`

- 以并行方式运行特定数量的 [j]obs（需要安装 GNU `parallel`）：

`bats --jobs {{number}} {{path/to/test.bats}}`