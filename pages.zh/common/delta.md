# delta

> Git 和 diff 输出的查看器。
> 另请参阅：`diff`, `difft`。
> 更多信息：<https://dandavison.github.io/delta/full---help-output.html>。

- 比较文件或目录：

`delta {{路径/到/旧文件或目录}} {{路径/到/新文件或目录}}`

- 比较文件或目录，显示行号：

`delta {{[-n|--line-numbers]}} {{路径/到/旧文件或目录}} {{路径/到/新文件或目录}}`

- 比较文件或目录，并排显示差异：

`delta {{[-s|--side-by-side]}} {{路径/到/旧文件或目录}} {{路径/到/新文件或目录}}`

- 比较文件或目录，忽略任何 Git 配置设置：

`delta --no-gitconfig {{路径/到/旧文件或目录}} {{路径/到/新文件或目录}}`

- 比较，根据终端模拟器的超链接规范，将提交哈希、文件名和行号渲染为超链接：

`delta --hyperlinks {{路径/到/旧文件或目录}} {{路径/到/新文件或目录}}`

- 显示当前设置：

`delta --show-config`

- 显示支持的语言及相关文件扩展名：

`delta --list-languages`
