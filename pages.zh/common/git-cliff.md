# git cliff

> 高度可定制的变更日志生成器。
> 更多信息：<https://git-cliff.org/docs/usage/args>.

- 从 Git 仓库中的所有提交生成变更日志并保存到 `CHANGELOG.md`：

`git cliff > {{CHANGELOG.md}}`

- 从最新标签开始的提交生成变更日志并输出到 `stdout`：

`git cliff {{[-l|--latest]}}`

- 从属于当前标签的提交生成变更日志（在执行此命令前使用 `git checkout` 切换到一个标签）：

`git cliff --current`

- 从不属于任何标签的提交生成变更日志：

`git cliff {{[-u|--unreleased]}}`

- 将默认配置文件写入当前目录的 `cliff.toml`：

`git cliff {{[-i|--init]}}`