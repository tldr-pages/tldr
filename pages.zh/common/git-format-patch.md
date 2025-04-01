# git format-patch

> 准备 .patch 文件。适用于通过电子邮件发送提交。
> 参见 `git am`，它可以应用生成的 .patch 文件。
> 更多信息：<https://git-scm.com/docs/git-format-patch>.

- 为所有未推送的提交创建自动命名的 `.patch` 文件：

`git format-patch {{origin}}`

- 将两个版本之间的所有提交写入到 `stdout` 的 `.patch` 文件中：

`git format-patch {{revision_1}}..{{revision_2}}`

- 为最新的 3 次提交写入 `.patch` 文件：

`git format-patch -{{3}}`
