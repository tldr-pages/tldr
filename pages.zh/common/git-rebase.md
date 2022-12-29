# git rebase

> 将 commits 从一个分支合并到另一个分支上。
> 常用于跨分支的 commits 合并，在被合并分支的最头部构建新的 `commit`，表示合并完成。
> 更多信息：<https://git-scm.com/docs/git-rebase>.

- 在另一个分支的头节点合并当前分支：

`git rebase {{目标分支}}`

- 启动交互式的合并任务，允许对提交的内容进行重新排序、省略、合并或修改：

`git rebase -i {{目标分支或 commit 的 hash}}`

- 处理完冲突文件后，继续执行合并任务：

`git rebase --continue`

- 跳过冲突文件，继续执行合并任务：

`git rebase --skip`

- 终止正在执行中的合并任务（例如：对于正处于解决冲突中的任务，将其打断，恢复到合并前的状态）：

`git rebase --abort`

- 将分支的部分 commits 生成新的 `commit`，移动到新分支的头节点：

`git rebase --onto {{目标分支}} {{当前分支}}`

- 启动交互式的合并任务，对最近提交的 5 个 commits 进行重新排序、省略、合并或修改：

`git rebase -i {{HEAD~5}}`

- 以当前分支优先的策略，自动处理分支间的冲突，执行合并：

`git rebase -X theirs {{分支名称}}`
