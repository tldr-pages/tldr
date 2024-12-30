# pushd

> 将一个目录放入堆栈，以便后续访问。
> 另见 `popd` 以切换回原始目录，以及 `dirs` 以显示目录堆栈内容。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>。

- 切换到目录并将其压入堆栈：

`pushd {{path/to/directory}}`

- 交换堆栈中的第一个和第二个目录：

`pushd`

- 通过将第5个元素置为堆栈顶部来旋转堆栈：

`pushd +4`

- 将堆栈向左旋转4次（当前目录保持在顶部，通过替换第5个元素）：

`pushd -n +4`