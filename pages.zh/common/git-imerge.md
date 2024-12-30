# git-imerge

> 在两个 Git 分支之间增量地执行合并或变基。
> 分支之间的冲突被追踪到个别提交对，以简化冲突解决。
> 更多信息：<https://github.com/mhagger/git-imerge>。

- 开始基于 imerge 的变基（首先检查要变基的分支）：

`git imerge rebase {{branch_to_rebase_onto}}`

- 开始基于 imerge 的合并（首先检查要合并到的分支）：

`git imerge merge {{branch_to_be_merged}}`

- 显示正在进行的合并或变基的 ASCII 图：

`git imerge diagram`

- 在解决冲突后继续 imerge 操作（首先 `git add` 冲突文件）：

`git imerge continue --no-edit`

- 在所有冲突解决后结束 imerge 操作：

`git imerge finish`

- 中止 imerge 操作，并返回到上一个分支：

`git-imerge remove && git checkout {{previous_branch}}`