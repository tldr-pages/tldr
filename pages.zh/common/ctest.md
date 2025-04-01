# ctest

> CMake 测试驱动程序。
> 更多信息：<https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest>。

- 运行 CMake 项目中定义的所有测试，同时并行执行 4 个任务：

`ctest -j{{4}} --output-on-failure`

- 列出可用的测试：

`ctest -N`

- 根据测试名称运行单个测试，或通过正则表达式进行过滤：

`ctest --output-on-failure -R '^{{test_name}}$'`
