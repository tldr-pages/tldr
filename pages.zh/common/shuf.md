# shuf

> 生成随机排列。
> 更多信息： <https://www.gnu.org/software/coreutils/shuf>。

- 随机化文件中行的顺序并输出结果：

`shuf {{path/to/file}}`

- 仅输出结果的前5个条目：

`shuf --head-count=5 {{path/to/file}}`

- 将输出写入另一个文件：

`shuf {{path/to/input_file}} --output={{path/to/output_file}}`

- 在1-10（包含）范围内生成3个随机数：

`shuf --head-count=3 --input-range=1-10 --repeat`