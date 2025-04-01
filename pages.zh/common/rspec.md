# rspec

> 用 Ruby 编写的以行为驱动开发的测试框架，用于测试 Ruby 代码。
> 更多信息：<https://rspec.info>.

- 初始化 .rspec 配置文件和 spec 辅助文件：

`rspec --init`

- 运行所有测试：

`rspec`

- 运行特定目录下的测试：

`rspec {{path/to/directory}}`

- 运行一个或多个测试文件：

`rspec {{path/to/file1 path/to/file2 ...}}`

- 运行文件中的特定测试（例如，测试从第 83 行开始）：

`rspec {{path/to/file}}:{{83}}`

- 使用特定的随机数种子运行测试：

`rspec --seed {{seed_number}}`
