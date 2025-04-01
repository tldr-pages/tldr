# snakefmt

> 格式化 Snakemake 文件。
> 更多信息：<https://github.com/snakemake/snakefmt>。

- 格式化特定的 Snakefile：

`snakefmt {{path/to/snakefile}}`

- 递归格式化特定目录中的所有 Snakefile：

`snakefmt {{path/to/directory}}`

- 使用特定配置文件格式化文件：

`snakefmt --config {{path/to/config.toml}} {{path/to/snakefile}}`

- 使用特定的最大行长度格式化文件：

`snakefmt --line-length {{100}} {{path/to/snakefile}}`

- 显示将要进行的更改但不执行（dry-run）：

`snakefmt --diff {{path/to/snakefile}}`