# ptx

> 从文本文件生成单词的混排索引。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/ptx-invocation.html>.

- 生成混排索引，其中每行的第一个字段是索引引用：

`ptx {{[-r|--references]}} {{path/to/file}}`

- 生成具有自动生成的索引引用的混排索引：

`ptx {{[-A|--auto-reference]}} {{path/to/file}}`

- 生成固定宽度的混排索引：

`ptx {{[-w|--width]}} {{width_in_columns}} {{path/to/file}}`

- 生成包含过滤词列表的混排索引：

`ptx {{[-o|--only-file]}} {{path/to/filter}} {{path/to/file}}`

- 生成具有 SYSV 风格行为的混排索引：

`ptx {{[-G|--traditional]}} {{path/to/file}}`
