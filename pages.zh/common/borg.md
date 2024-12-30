# borg

> 去重备份工具。
> 创建可作为文件系统挂载的本地或远程备份。
> 更多信息：<https://borgbackup.readthedocs.io/en/stable/usage/general.html>。

- 初始化一个（本地）库：

`borg init {{path/to/repo_directory}}`

- 将一个目录备份到库中，创建一个名为“Monday”的档案：

`borg create --progress {{path/to/repo_directory}}::{{Monday}} {{path/to/source_directory}}`

- 列出库中的所有档案：

`borg list {{path/to/repo_directory}}`

- 从远程库中的“Monday”档案中提取特定目录，排除所有 `*.ext` 文件：

`borg extract {{user}}@{{host}}:{{path/to/repo_directory}}::{{Monday}} {{path/to/target_directory}} --exclude '{{*.ext}}'`

- 通过删除所有超过7天的档案来修剪库，并列出变更：

`borg prune --keep-within {{7d}} --list {{path/to/repo_directory}}`

- 将库挂载为FUSE文件系统：

`borg mount {{path/to/repo_directory}}::{{Monday}} {{path/to/mountpoint}}`

- 显示有关创建档案的帮助：

`borg create --help`