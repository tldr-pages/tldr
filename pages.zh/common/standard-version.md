# standard-version

> 自动化版本管理和变更日志生成，支持 SemVer 和 Conventional Commits。
> 更多信息：<https://github.com/conventional-changelog/standard-version>。

- 更新变更日志文件并打上发布标签：

`standard-version`

- 打上发布标签但不提升版本：

`standard-version --first-release`

- 更新变更日志并打上 alpha 版发布标签：

`standard-version --prerelease alpha`

- 更新变更日志并打上特定类型的发布标签：

`standard-version --release-as {{major|minor|patch}}`

- 打上发布标签，在提交步骤中防止钩子被验证：

`standard-version --no-verify`

- 打上发布标签，提交所有已暂存的更改，而不仅仅是 `standard-version` 影响的文件：

`standard-version --commit-all`

- 更新特定的变更日志文件并打上发布标签：

`standard-version --infile {{path/to/file.md}}`

- 显示将要执行的发布，但不实际执行：

`standard-version --dry-run`