# phpstan

> PHP 静态分析工具，用于发现代码中的错误。
> 更多信息：<https://phpstan.org/user-guide/command-line-usage>.

- 分析一个或多个目录：

`phpstan analyse {{path/to/directory1 path/to/directory2 ...}}`

- 使用配置文件分析目录：

`phpstan analyse {{path/to/directory}} {{[-c|--configuration]}} {{path/to/config}}`

- 使用特定的规则级别（0-10，数字越大越严格）进行分析：

`phpstan analyse {{path/to/directory}} {{[-l|--level]}} {{level}}`

- 指定一个在分析前加载的自动加载文件：

`phpstan analyse {{path/to/directory}} {{[-a|--autoload-file]}} {{path/to/autoload_file}}`

- 在分析时指定内存限制：

`phpstan analyse {{path/to/directory}} --memory-limit {{memory_limit}}`

- 显示分析可用的选项：

`phpstan analyse --help`
