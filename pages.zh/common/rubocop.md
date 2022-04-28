# rubocop

> 格式化 Ruby 文件。
> 更多信息：<https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- 检查当前目录中的所有文件（包括子目录）：

`rubocop`

- 检查一个或多个指定文件或目录：

`rubocop {{目录 / 文件名}} {{目录 /}}`

- 将输出写入指定文件：

`rubocop --out {{目录 / 文件名}}`

- 查看规则列表（格式化规则）：

`rubocop --show-cops`

- 排除格式规则：

`rubocop --except {{规则 1}} {{规则 2}}`

- 只运行指定的规则：

`rubocop --only {{规则 1}} {{规则 2}}`

- 自动更正文件（实验）：

`rubocop --auto-correct`
