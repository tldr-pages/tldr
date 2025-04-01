# bup

> 基于 Git 包文件格式的备份系统，提供增量备份和全局去重。
> 更多信息：<https://manned.org/bup>.

- 在指定的本地目录中初始化备份仓库：

`bup {{[-d|--bup-dir]}} {{path/to/repository}} init`

- 在进行备份之前准备指定的目录：

`bup {{[-d|--bup-dir]}} {{path/to/repository}} index {{path/to/directory}}`

- 将目录备份到仓库并指定其名称：

`bup {{[-d|--bup-dir]}} {{path/to/repository}} save {{[-n|--name]}} {{backup_name}} {{path/to/directory}}`

- 显示仓库中当前存储的备份快照：

`bup {{[-d|--bup-dir]}} {{path/to/repository}} ls`

- 将特定的备份快照恢复到目标目录：

`bup {{[-d|--bup-dir]}} {{path/to/repository}} restore {{[-C|--outdir]}} {{path/to/target_directory}} {{backup_name}}`