# lit

> LLVM 集成测试工具，用于执行 LLVM 和 Clang 风格的测试套件并汇总结果。
> 是 LLVM 的一部分。
> 更多信息：<https://www.llvm.org/docs/CommandGuide/lit.html>。

- 运行指定的测试用例：

`lit {{path/to/test_file.test}}`

- 运行指定目录中的所有测试用例：

`lit {{path/to/test_suite}}`

- 运行所有测试用例并检查每个用例的运行时间，然后在汇总输出中报告：

`lit {{path/to/test_suite}} --time-tests`

- 使用 Valgrind（内存检查和内存泄漏测试）运行单个测试：

`lit {{path/to/test_file.test}} --vg --vg-leak --vg-args={{args_to_valgrind}}`
