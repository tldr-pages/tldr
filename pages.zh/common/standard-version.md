# standard-version

> 自动化版本控制和变更日志生成，使用SemVer和传统提交。
> 更多信息：<https://github.com/conventional-changelog/standard-version>。

- 更新变更日志文件并标记一个发布版本：

`standard-version`

- 标记一个发布版本而不提升版本：

`standard-version --first-release`

- 更新变更日志并标记一个alpha发布版本：

`standard-version --prerelease alpha`

- 更新变更日志并标记特定的发布类型：

`standard-version --release-as {{major|minor|patch}}`

- 标记一个发布版本，防止在提交步骤中验证钩子：

`standard-version --no-verify`

- 标记一个发布版本，提交所有暂存的更改，而不仅仅是受`standard-version`影响的文件：

`standard-version --commit-all`

- 更新特定的变更日志文件并标记一个发布版本：

`standard-version --infile {{path/to/file.md}}`

- 显示将要执行的发布版本，但不实际执行：

`standard-version --dry-run`