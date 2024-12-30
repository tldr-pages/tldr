# bup

> 基于 Git 打包文件格式的备份系统，提供增量保存和全局去重功能。
> 更多信息请访问: <https://github.com/bup/bup>。

- 在给定的本地[d]irectory中初始化一个备份库：

`bup -d {{path/to/repository}} init`

- 在进行备份之前准备一个给定的[d]irectory：

`bup -d {{path/to/repository}} index {{path/to/directory}}`

- 将一个[d]irectory备份到指定名称的库中：

`bup -d {{path/to/repository}} save -n {{backup_name}} {{path/to/directory}}`

- 显示当前存储在库中的备份快照：

`bup -d {{path/to/repository}} ls`

- 将特定的备份快照恢复到目标目录[C]：

`bup -d {{path/to/repository}} restore -C {{path/to/target_directory}} {{backup_name}}`