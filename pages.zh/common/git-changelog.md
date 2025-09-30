# git changelog

> 从仓库提交和标签生成变更日志报告。
> 属于 `git-extras` 的一部分。
> 更多信息：<https://manned.org/git-changelog>.

- 更新现有文件或创建新的 `History.md` 文件，包含自最新 Git 标签以来的提交信息：

`git changelog`

- 列出当前版本的提交：

`git changelog {{[-l|--list]}}`

- 列出从标签 `2.1.0` 到现在的提交范围

`git changelog {{[-l|--list]}} {{[-s|--start-tag]}} {{2.1.0}}`

- 以美观格式列出标签 `0.5.0` 到 `1.0.0` 之间的提交：

`git changelog {{[-s|--start-tag]}} {{0.5.0}} {{[-f|--final-tag]}} {{1.0.0}}`

- 以美观格式列出提交 `0b97430` 到标签 `1.0.0` 之间的提交：

`git changelog --start-commit {{0b97430}} {{[-f|--final-tag]}} {{1.0.0}}`

- 指定 `CHANGELOG.md` 作为输出文件：

`git changelog {{CHANGELOG.md}}`

- 完全替换当前变更日志文件的内容：

`git changelog {{[-p|--prune-old]}}`
