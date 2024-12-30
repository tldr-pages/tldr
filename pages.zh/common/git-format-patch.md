# git format-patch

> 准备 .patch 文件。将提交通过邮件发送到其他地方时很有用。
> 另请参见 `git am`，它可以应用生成的 .patch 文件。
> 更多信息：<https://git-scm.com/docs/git-format-patch>。

- 为所有未推送的提交创建一个自动命名的 `.patch` 文件：

`git format-patch {{origin}}`

- 将两个修订版本之间的所有提交写入 `.patch` 文件并输出到 `stdout`：

`git format-patch {{revision_1}}..{{revision_2}}`

- 为最新的 3 个提交写入 `.patch` 文件：

`git format-patch -{{3}}`