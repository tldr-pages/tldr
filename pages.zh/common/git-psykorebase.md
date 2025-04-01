# git psykorebase

> 使用合并提交和仅一次冲突处理将一个分支变基到另一个分支上。
> 这是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-psykorebase>.

- 使用合并提交和仅一次冲突处理将当前分支变基到另一个分支上：

`git psykorebase {{upstream_branch}}`

- 解决冲突后继续：

`git psykorebase --continue`

- 指定要变基的分支：

`git psykorebase {{upstream_branch}} {{target_branch}}`
