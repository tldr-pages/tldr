# getopt

> 解析命令行参数。
> 更多信息: <https://www.gnu.org/software/libc/manual/html_node/Getopt.html>。

- 使用简写解析可选的 `verbose`/`version` 标志：

`getopt --options vV --longoptions verbose,version -- --version --verbose`

- 添加一个带有必需参数的 `--file` 选项，简写为 `-f`：

`getopt --options f: --longoptions file: -- --file=somefile`

- 添加一个带有可选参数的 `--verbose` 选项，简写为 `-v`，并传递一个非选项参数 `arg`：

`getopt --options v:: --longoptions verbose:: -- --verbose arg`

- 接受 `-r` 和 `--verbose` 标志，添加一个带有可选参数的 `--accept` 选项，并添加一个带有必需参数的 `--target` 选项，简写为：

`getopt --options rv::s::t: --longoptions verbose,source::,target: -- -v --target target`