# phpstan

> 一个用于发现代码中错误的 PHP 静态分析工具。
> 更多信息：<https://github.com/phpstan/phpstan>。

- 分析一个或多个目录：

`phpstan analyse {{path/to/directory1 path/to/directory2 ...}}`

- 使用配置文件分析目录：

`phpstan analyse {{path/to/directory}} --configuration {{path/to/config}}`

- 使用特定的规则级别进行分析（0-7，级别越高越严格）：

`phpstan analyse {{path/to/directory}} --level {{level}}`

- 指定在分析前加载的自动加载文件：

`phpstan analyse {{path/to/directory}} --autoload-file {{path/to/autoload_file}}`

- 在分析过程中指定内存限制：

`phpstan analyse {{path/to/directory}} --memory-limit {{memory_limit}}`

- 显示可用的分析选项：

`phpstan analyse --help`