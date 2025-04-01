# getopt

> 解析命令行参数。
> 更多信息：<https://manned.org/getopt>.

- 解析可选的 `verbose`/`version` 标志及其简写：

`getopt {{[-o|--options]}} vV {{[-l|--longoptions]}} verbose,version -- --version --verbose`

- 添加一个带必需参数的 `--file` 选项，简写为 `-f`：

`getopt {{[-o|--options]}} f: {{[-l|--longoptions]}} file: -- --file=somefile`

- 添加一个带可选参数的 `--verbose` 选项，简写为 `-v`，并传递一个非选项参数 `arg`：

`getopt {{[-o|--options]}} v:: {{[-l|--longoptions]}} verbose:: -- --verbose arg`

- 接受 `-r` 和 `--verbose` 标志，一个带可选参数的 `--accept` 选项，以及带有简写 `-t` 的带必需参数的 `--target` 选项：

`getopt {{[-o|--options]}} rv::s::t: {{[-l|--longoptions]}} verbose,source::,target: -- -v --target target`
