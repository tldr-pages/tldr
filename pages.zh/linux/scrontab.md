# scrontab

> 管理 Slurm crontab 文件。
> 更多信息：<https://slurm.schedmd.com/scrontab.html>。

- 从指定文件安装新的 crontab：

`scrontab {{path/to/file}}`

- [e]dit 当前用户的 crontab：

`scrontab -e`

- [e]dit 指定用户的 crontab：

`scrontab --user={{user_id}} -e`

- [r]emove 当前的 crontab：

`scrontab -r`

- 将当前用户的 crontab 打印到 `stdout`：

`scrontab -l`