# ruff check

> 极速 Python 代码检查工具。`check` 是默认命令 - 可以在任何地方省略。
> 如果未指定文件或目录，默认使用当前工作目录。
> 更多信息：<https://docs.astral.sh/ruff/linter>。

- 在指定的文件或目录上运行代码检查：

`ruff check {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 应用建议的修复，直接修改文件：

`ruff check --fix`

- 运行代码检查并在文件更改时重新检查：

`ruff check --watch`

- 仅启用指定的规则（或所有规则），忽略配置文件：

`ruff check --select {{ALL|rule_code1,rule_code2,...}}`

- 额外启用指定的规则：

`ruff check --extend-select {{rule_code1,rule_code2,...}}`

- 禁用指定的规则：

`ruff check --ignore {{rule_code1,rule_code2,...}}`

- 通过在所有违反规则的行中添加 `# noqa` 指令来忽略所有现有的规则违规：

`ruff check --select {{rule_code}} --add-noqa`