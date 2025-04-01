# scrontab

> 管理 Slurm crontab 文件。
> 更多信息：<https://slurm.schedmd.com/scrontab.html>。

- 从指定的文件安装新的 crontab：

`scrontab {{path/to/file}}`

- [编辑]当前用户的 crontab：

`scrontab -e`

- [编辑]指定用户的 crontab：

`scrontab --user={{user_id}} -e`

- [移除]当前用户的 crontab：

`scrontab -r`

- 将当前用户的 crontab 打印到 `stdout`：

`scrontab -l`