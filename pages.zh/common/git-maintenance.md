# git-maintenance

> 执行任务以优化 Git 仓库数据。
> 更多信息：<https://git-scm.com/docs/git-maintenance>。

- 将当前仓库注册到用户的仓库列表中，以便每天执行维护：

`git maintenance register`

- 安排每小时对当前仓库执行维护任务：

`git maintenance start`

- 停止当前仓库的后台维护计划：

`git maintenance stop`

- 从用户的维护仓库列表中移除当前仓库：

`git maintenance unregister`

- 在当前仓库上运行特定的维护任务：

`git maintenance run --task {{commit-graph|gc|incremental-repack|loose-objects|pack-refs|prefetch}}`