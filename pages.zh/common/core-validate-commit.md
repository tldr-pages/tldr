# core-validate-commit

> 验证 Node.js 核心的提交消息。
> 更多信息：<https://github.com/nodejs/core-validate-commit>。

- 验证当前提交：

`core-validate-commit`

- 验证特定的提交：

`core-validate-commit {{commit_hash}}`

- 验证一系列提交：

`git rev-list {{commit_hash}}..HEAD | xargs core-validate-commit`

- 列出所有验证规则：

`core-validate-commit --list`

- 列出所有有效的 Node.js 子系统：

`core-validate-commit --list-subsystem`

- 以 tap 格式验证当前提交的输出：

`core-validate-commit --tap`

- 显示帮助信息：

`core-validate-commit --help`