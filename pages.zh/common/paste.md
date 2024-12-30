# paste

> 合并文件的行。
> 更多信息：<https://www.gnu.org/software/coreutils/paste>。

- 将所有行合并为一行，使用 TAB 作为分隔符：

`paste -s {{path/to/file}}`

- 将所有行合并为一行，使用指定的分隔符：

`paste -s -d {{delimiter}} {{path/to/file}}`

- 将两个文件并排合并，每个文件在其列中，使用 TAB 作为分隔符：

`paste {{path/to/file1}} {{path/to/file2}}`

- 将两个文件并排合并，每个文件在其列中，使用指定的分隔符：

`paste -d {{delimiter}} {{path/to/file1}} {{path/to/file2}}`

- 交替合并两个文件的行：

`paste -d '\n' {{path/to/file1}} {{path/to/file2}}`