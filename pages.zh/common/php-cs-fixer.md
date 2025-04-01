# PHP-CS-Fixer

> PHP 代码风格自动修复工具。
> 更多信息：<https://github.com/FriendsOfPHP/PHP-CS-Fixer>。

- 在当前目录执行代码风格修复：

`php-cs-fixer fix`

- 为指定目录执行代码风格修复：

`php-cs-fixer fix {{path/to/directory}}`

- 执行代码风格检查但不应用更改：

`php-cs-fixer fix --dry-run`

- 使用特定规则执行代码风格修复：

`php-cs-fixer fix --rules={{rules}}`

- 显示已应用的规则：

`php-cs-fixer fix --verbose`

- 以不同的格式输出结果：

`php-cs-fixer fix --format={{txt|json|xml|checkstyle|junit|gitlab}}`

- 显示需要修复的文件：

`php-cs-fixer list-files`

- 描述某个规则或规则集：

`php-cs-fixer describe {{rule}}`