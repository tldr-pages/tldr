# git rebase

> 将一个分支的提交重新应用到另一个分支之上。
> 通常用于“移动”整个分支到另一个基础上，在新位置创建提交的副本。
> 更多信息：<https://git-scm.com/docs/git-rebase>。

- 将当前分支重新基于另一个指定的分支：

`git rebase {{new_base_branch}}`

- 启动一个交互式变基，允许重新排序、忽略、合并或修改提交：

`git rebase {{-i|--interactive}} {{target_base_branch_or_commit_hash}}`

- 继续一个因合并失败而中断的变基，在编辑冲突文件后：

`git rebase --continue`

- 继续一个因合并冲突而暂停的变基，通过跳过冲突的提交：

`git rebase --skip`

- 中止一个正在进行的变基（例如，如果它因合并冲突而中断）：

`git rebase --abort`

- 将当前分支的一部分移动到一个新的基础上，提供旧的基础作为起点：

`git rebase --onto {{new_base}} {{old_base}}`

- 在原地重新应用最后 5 个提交，暂停以允许它们被重新排序、忽略、合并或修改：

`git rebase {{-i|--interactive}} {{HEAD~5}}`

- 通过优先使用工作分支版本自动解决任何冲突（在这种情况下，`theirs` 关键字的含义是相反的）：

`git rebase {{-X|--strategy-option}} theirs {{branch_name}}`