# git-imerge

> 在两个 Git 分支之间逐步执行合并或变基。
> 分支之间的冲突被追踪到单个提交对，以简化冲突解决。
> 更多信息：<https://github.com/mhagger/git-imerge>。

- 开始基于 imerge 的变基（首先检出要变基的分支）：

`git imerge rebase {{要变基到的分支}}`

- 开始基于 imerge 的合并（首先检出要合并到的分支）：

`git imerge merge {{要合并的分支}}`

- 显示正在进行的合并或变基的 ASCII 图：

`git imerge diagram`

- 解决冲突后继续 imerge 操作（首先使用 `git add` 添加冲突文件）：

`git imerge continue --no-edit`

- 解决所有冲突后完成 imerge 操作：

`git imerge finish`

- 中止 imerge 操作，并返回到上一个分支：

`git-imerge remove && git checkout {{上一个分支}}`
