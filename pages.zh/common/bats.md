# bats

> Bash 自动化测试系统：符合 TAP（<https://testanything.org/>）的 Bash 测试框架。
> 更多信息：<https://bats-core.readthedocs.io/en/stable/usage.html>。

- 运行 BATS 测试脚本并以 TAP（Test Anything Protocol）格式输出结果：

`bats {{[-t|--tap]}} {{路径/到/test.bats}}`

- 计算测试脚本的测试用例数量而不运行任何测试：

`bats {{[-c|--count]}} {{路径/到/test.bats}}`

- 递归运行 BATS 测试用例（扩展名为 `.bats` 的文件）：

`bats {{[-r|--recursive]}} {{路径/到/目录}}`

- 以特定格式输出结果：

`bats {{[-F|--formatter]}} {{pretty|tap|tap13|junit}} {{路径/到/test.bats}}`

- 为测试添加计时信息：

`bats {{[-T|--timing]}} {{路径/到/test.bats}}`

- 并行运行特定数量的作业（需要安装 GNU `parallel`）：

`bats {{[-j|--jobs]}} {{数量}} {{路径/到/test.bats}}`
