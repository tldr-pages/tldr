# popd

> 通过 pushd shell 内置程序删除目录堆栈中的目录。
> 另见 `pushd` 将目录放入堆栈和 `dirs` 显示目录堆栈内容。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-popd>.

- 从堆栈中删除顶部目录，并用 `cd` 跳转到该目录：

`popd`

- 删除第 N 个目录（从零开始，以用 `dirs` 打印的列表左侧开始）：

`popd +N`

- 删除第 N 个目录（从零开始，以用 `dirs` 打印的列表右侧开始）：

`popd -N`

- 删除第 1 个目录（从零开始，以用 `dirs` 打印的列表左侧开始）：

`popd -n`
