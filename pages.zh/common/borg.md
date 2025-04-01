# borg

> 重复数据删除备份工具。
> 创建可作为文件系统挂载的本地或远程备份。
> 更多信息：<https://borgbackup.readthedocs.io/en/stable/usage/general.html>。

- 初始化一个（本地）仓库：

`borg init {{path/to/repo_directory}}`

- 将一个目录备份到仓库中，创建名为 "Monday" 的归档：

`borg create --progress {{path/to/repo_directory}}::{{Monday}} {{path/to/source_directory}}`

- 列出仓库中的所有归档：

`borg list {{path/to/repo_directory}}`

- 从远程仓库的 "Monday" 归档中提取特定目录，排除所有 `*.ext` 文件：

`borg extract {{user}}@{{host}}:{{path/to/repo_directory}}::{{Monday}} {{path/to/target_directory}} --exclude '{{*.ext}}'`

- 通过删除所有超过 7 天的归档来清理仓库，列出更改：

`borg prune --keep-within {{7d}} --list {{path/to/repo_directory}}`

- 将仓库作为 FUSE 文件系统挂载：

`borg mount {{path/to/repo_directory}}::{{Monday}} {{path/to/mountpoint}}`

- 显示创建归档的帮助信息：

`borg create --help`