# prqlc

> PRQL 编译器。
> PRQL 是一种现代的数据转换语言，简单、强大，可以替代 SQL。
> 更多信息：<https://prql-lang.org>。

- 以交互模式运行编译器：

`prqlc compile`

- 将特定的 `.prql` 文件编译到标准输出：

`prqlc compile {{path/to/file.prql}}`

- 将 `.prql` 文件编译为 `.sql` 文件：

`prqlc compile {{path/to/source.prql}} {{path/to/target.sql}}`

- 编译一个查询：

`echo "{{from employees | filter has_dog | select salary}}" | prqlc compile`

- 监视目录并在文件修改时编译：

`prqlc watch {{path/to/directory}}`