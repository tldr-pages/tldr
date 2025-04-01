# phpmd

> PHP 代码检测工具：检查常见的潜在问题。
> 更多信息：<https://github.com/phpmd/phpmd>.

- 显示可用的规则集和格式列表：

`phpmd`

- 使用逗号分隔的规则集扫描文件或目录中的问题：

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}}`

- 指定规则的最小优先级阈值：

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --minimumpriority {{priority}}`

- 只包括指定的扩展名进行分析：

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --suffixes {{extensions}}`

- 排除指定的逗号分隔的目录：

`phpmd {{path/to/file_or_directory1,path/to/file_or_directory2,...}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --exclude {{directory_patterns}}`

- 将结果输出到文件而不是 `stdout`：

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --reportfile {{path/to/report_file}}`

- 忽略使用抑制警告的 PHPDoc 注释：

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --strict`