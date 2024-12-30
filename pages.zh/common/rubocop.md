# rubocop

> 检查 Ruby 文件。
> 更多信息：<https://docs.rubocop.org/rubocop/usage/basic_usage.html>。

- 检查当前目录（包括子目录）中的所有文件：

`rubocop`

- 检查一个或多个特定文件或目录：

`rubocop {{路径/到/文件_或_目录1 路径/到/文件_或_目录2 ...}}`

- 将输出写入文件：

`rubocop --out {{路径/到/文件}}`

- 查看警察（lint 规则）列表：

`rubocop --show-cops`

- 排除一个警察：

`rubocop --except {{警察1 警察2 ...}}`

- 仅运行指定的警察：

`rubocop --only {{警察1 警察2 ...}}`

- 自动修正文件（实验性）：

`rubocop --auto-correct`