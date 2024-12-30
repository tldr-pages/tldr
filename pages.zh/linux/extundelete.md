# extundelete

> 从 ext3 或 ext4 分区恢复已删除的文件，方法是解析日志。
> 另请参见 `date` 以获取 Unix 时间信息，以及 `umount` 以卸载分区。
> 更多信息请访问：<https://extundelete.sourceforge.net>。

- 恢复设备 X 上分区 N 中的所有已删除文件：

`sudo extundelete {{/dev/sdXN}} --restore-all`

- 从相对于根的路径恢复一个文件（路径不要以 `/` 开头）：

`extundelete {{/dev/sdXN}} --restore-file {{path/to/file}}`

- 从相对于根的路径恢复一个目录（路径不要以 `/` 开头）：

`extundelete {{/dev/sdXN}} --restore-directory {{path/to/directory}}`

- 恢复 2020 年 1 月 1 日之后删除的所有文件（以 Unix 时间表示）：

`extundelete {{/dev/sdXN}} --restore-all --after {{1577840400}}`