# git 批量操作

> 在多个 Git 仓库上执行操作。
> 是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>。

- 将当前目录注册为工作区：

`git bulk --addcurrent {{workspace_name}}`

- 注册一个用于批量操作的工作区：

`git bulk --addworkspace {{workspace_name}} {{/absolute/path/to/repository}}`

- 在特定目录中克隆一个仓库，然后将该仓库注册为工作区：

`git bulk --addworkspace {{workspace_name}} {{/absolute/path/to/parent_directory}} --from {{remote_repository_location}}`

- 从以换行符分隔的远程位置列表中克隆仓库，然后将它们注册为工作区：

`git bulk --addworkspace {{workspace_name}} {{/path/to/root/directory}} --from {{/path/to/file}}`

- 列出所有已注册的工作区：

`git bulk --listall`

- 在当前工作区的仓库上运行 Git 命令：

`git bulk {{command}} {{command_arguments}}`

- 移除特定工作区：

`git bulk --removeworkspace {{workspace_name}}`

- 移除所有工作区：

`git bulk --purge`