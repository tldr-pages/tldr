# shuf

> 生成随机排列。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/shuf-invocation.html>.

- 随机化文件中的行顺序并输出结果：

`shuf {{path/to/file}}`

- 仅输出结果的前5个条目：

`shuf {{[-n|--head-count]}} 5 {{path/to/file}}`

- 将输出写入另一个文件：

`shuf {{path/to/input_file}} {{[-o|--output]}} {{path/to/output_file}}`

- 生成1到10（包含）之间的3个随机数：

`shuf {{[-n|--head-count]}} 3 {{[-i|--input-range]}} 1-10 {{[-r|--repeat]}}`