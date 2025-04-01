# phan

> 一个 PHP 的静态分析工具。
> 更多信息：<https://github.com/phan/phan>.

- 在当前目录生成一个 `.phan/config.php` 文件：

`phan --init`

- 使用指定的级别生成 Phan 配置文件（1 级最严格，5 级最宽松）：

`phan --init --init-level {{level}}`

- 分析当前目录：

`phan`

- 分析一个或多个目录：

`phan --directory {{path/to/directory}} --directory {{path/to/another_directory}}`

- 指定配置文件（默认为 `.phan/config.php`）：

`phan --config-file {{path/to/config.php}}`

- 指定输出模式：

`phan --output-mode {{text|verbose|json|csv|codeclimate|checkstyle|pylint|html}}`

- 指定并行进程的数量：

`phan --processes {{number_of_processes}}`
