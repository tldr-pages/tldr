# extundelete

> 通过解析日志从 ext3 或 ext4 分区恢复已删除的文件。
> 参见 `date` 以获取 Unix 时间信息，以及 `umount` 用于卸载分区。
> 更多信息：<https://extundelete.sourceforge.net>.

- 恢复设备 X 上分区 N 中所有已删除的文件：

`sudo extundelete {{/dev/sdXN}} --restore-all`

- 从相对于根目录的路径恢复文件（路径不要以 `/` 开头）：

`extundelete {{/dev/sdXN}} --restore-file {{path/to/file}}`

- 从相对于根目录的路径恢复目录（路径不要以 `/` 开头）：

`extundelete {{/dev/sdXN}} --restore-directory {{path/to/directory}}`

- 恢复 2020 年 1 月 1 日后（Unix 时间）删除的所有文件：

`extundelete {{/dev/sdXN}} --restore-all --after {{1577840400}}`
