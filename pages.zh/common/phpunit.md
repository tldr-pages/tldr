# phpunit

> PHPUnit 命令行测试运行器。
> 更多信息：<https://phpunit.de>。

- 在当前目录中运行测试。注意：需要你有一个 'phpunit.xml' 文件：

`phpunit`

- 在特定文件中运行测试：

`phpunit {{path/to/TestFile.php}}`

- 运行带有指定分组注释的测试：

`phpunit --group {{name}}`

- 运行测试并生成 HTML 格式的覆盖率报告：

`phpunit --coverage-html {{path/to/directory}}`