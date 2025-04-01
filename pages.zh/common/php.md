# php

> PHP 命令行接口。
> 更多信息：<https://php.net>。

- 解析并执行 PHP 脚本：

`php {{path/to/file}}`

- 检查 PHP 脚本的语法（即进行语法检查）：

`php -l {{path/to/file}}`

- 以交互方式运行 PHP：

`php -a`

- 运行 PHP 代码（注意：不要使用 `<? ?>` 标签；使用反斜杠转义双引号）：

`php -r "{{code}}"`

- 在当前目录启动 PHP 内置 Web 服务器：

`php -S {{host:port}}`

- 列出已安装的 PHP 扩展：

`php -m`

- 显示当前 PHP 配置的信息：

`php -i`

- 显示特定函数的信息：

`php --rf {{function_name}}`