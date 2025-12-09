# pushd

> 将目录放在堆栈上，以便以后访问。
> 另见 `popd` 切换回原始目录和 `dirs` 显示目录堆栈内容。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-pushd>.

- 切换到目录并将其添加到堆栈上：

`pushd {{路径/到/目录}}`

- 切换堆栈上的第一个和第二个目录：

`pushd`

- 通过使第 5 个元素成为堆栈的顶部来旋转堆栈：

`pushd +4`

- 将堆栈向左旋转 4 次（当前目录通过替换第 5 个元素保持在顶部）：

`pushd -n +4`
