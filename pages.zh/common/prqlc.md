# prqlc

> PRQL 编译器。
> PRQL 是一种现代数据转换语言 - 一种简单、强大、管道式的 SQL 替代品。
> 更多信息请访问：<https://prql-lang.org>。

- 以交互方式运行编译器：

`prqlc compile`

- 将特定的 `.prql` 文件编译到 `stdout`：

`prqlc compile {{path/to/file.prql}}`

- 将 `.prql` 文件编译为 `.sql` 文件：

`prqlc compile {{path/to/source.prql}} {{path/to/target.sql}}`

- 编译查询：

`echo "{{from employees | filter has_dog | select salary}}" | prqlc compile`

- 监视目录并在文件修改时编译：

`prqlc watch {{path/to/directory}}`