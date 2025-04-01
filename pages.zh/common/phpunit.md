# phpunit

> PHPUnit 命令行测试运行器。
> 更多信息：<https://phpunit.de>。

- 运行当前目录中的测试。注意：需要存在一个 'phpunit.xml' 文件：

`phpunit`

- 运行特定文件中的测试：

`phpunit {{path/to/TestFile.php}}`

- 运行带有指定组注解的测试：

`phpunit --group {{name}}`

- 运行测试并生成 HTML 覆盖报告：

`phpunit --coverage-html {{path/to/directory}}`
