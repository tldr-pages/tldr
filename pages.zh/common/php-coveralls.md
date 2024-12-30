# php-coveralls

> Coveralls 的 PHP 客户端。
> 更多信息：<https://php-coveralls.github.io/php-coveralls>。

- 将覆盖率信息发送到 Coveralls：

`php-coveralls`

- 将特定目录的覆盖率信息发送到 Coveralls：

`php-coveralls --root_dir {{path/to/directory}}`

- 使用特定配置将覆盖率信息发送到 Coveralls：

`php-coveralls --config {{path/to/.coveralls.yml}}`

- 以详细输出的方式将覆盖率信息发送到 Coveralls：

`php-coveralls --verbose`

- 将不含可执行语句的源文件排除在外，发送覆盖率信息到 Coveralls：

`php-coveralls --exclude-no-stmt`

- 使用特定环境名称发送覆盖率信息到 Coveralls：

`php-coveralls --env {{test|dev|prod}}`

- 指定多个 Coverage Clover XML 文件进行上传：

`php-coveralls --coverage_clover {{path/to/first_clover.xml}} --coverage_clover {{path/to/second_clover.xml}}`

- 将将要发送到 Coveralls 的 JSON 输出到特定文件：

`php-coveralls --json_path {{path/to/coveralls-upload.json}}`