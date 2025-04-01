# php-coveralls

> 用于 Coveralls 的 PHP 客户端。
> 更多信息：<https://php-coveralls.github.io/php-coveralls>.

- 将代码覆盖率信息发送到 Coveralls：

`php-coveralls`

- 将指定目录的代码覆盖率信息发送到 Coveralls：

`php-coveralls --root_dir {{path/to/directory}}`

- 使用特定配置文件将代码覆盖率信息发送到 Coveralls：

`php-coveralls --config {{path/to/.coveralls.yml}}`

- 以详细模式将代码覆盖率信息发送到 Coveralls：

`php-coveralls --verbose`

- 排除没有可执行语句的源文件，将代码覆盖率信息发送到 Coveralls：

`php-coveralls --exclude-no-stmt`

- 使用特定环境名称将代码覆盖率信息发送到 Coveralls：

`php-coveralls --env {{test|dev|prod}}`

- 指定多个 Coverage Clover XML 文件以上传：

`php-coveralls --coverage_clover {{path/to/first_clover.xml}} --coverage_clover {{path/to/second_clover.xml}}`

- 将要发送到 Coveralls 的 JSON 输出到特定文件：

`php-coveralls --json_path {{path/to/coveralls-upload.json}}`