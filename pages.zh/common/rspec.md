# rspec

> 用于测试 Ruby 代码的以行为驱动开发为基础的测试框架，使用 Ruby 编写。
> 更多信息：<https://rspec.info>。

- 初始化 .rspec 配置和规范助手文件：

`rspec --init`

- 运行所有测试：

`rspec`

- 运行特定目录的测试：

`rspec {{path/to/directory}}`

- 运行一个或多个测试文件：

`rspec {{path/to/file1 path/to/file2 ...}}`

- 在文件中运行特定测试（例如，测试从第 83 行开始）：

`rspec {{path/to/file}}:{{83}}`

- 以特定种子运行规范：

`rspec --seed {{seed_number}}`