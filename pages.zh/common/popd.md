# popd

> 通过 pushd shell 内置程序删除目录堆栈中的目录。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- 从堆栈中删除顶部目录，并用 `cd` 跳转到该目录：

`popd`

- 删除第 n 个目录（从零开始，以用 `dirs` 打印的列表左侧开始）：

`popd +N`

- 删除第 n 个目录（从零开始，以用 `dirs` 打印的列表右侧开始）：

`popd -N`
