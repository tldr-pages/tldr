# parallel-lint

> 并行检查 PHP 文件的语法。
> 更多信息：<https://github.com/JakubOnderka/PHP-Parallel-Lint>。

- 检查特定目录的语法：

`parallel-lint {{path/to/directory}}`

- 使用指定数量的并行进程检查目录的语法：

`parallel-lint -j {{processes}} {{path/to/directory}}`

- 检查一个目录，排除指定的目录：

`parallel-lint --exclude {{path/to/excluded_directory}} {{path/to/directory}}`

- 使用逗号分隔的扩展名列表检查一个目录的文件：

`parallel-lint -e {{php,html,phpt}} {{path/to/directory}}`

- 检查一个目录并将结果输出为 JSON 格式：

`parallel-lint --json {{path/to/directory}}`

- 检查一个目录并显示包含错误的行的 Git Blame 结果：

`parallel-lint --blame {{path/to/directory}}`