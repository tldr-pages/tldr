# slurmdbd

> 为 Slurm 提供的安全企业级数据库接口。
> 更多信息：<https://slurm.schedmd.com/slurmdbd.html>.

- 将守护进程的 nice 值设置为指定的值，通常为负数：

`slurmdbd -n {{value}}`

- 将 `slurmdbd` 的工作目录更改为 LogFile 路径或 `/var/tmp`：

`slurmdbd -s`

- 显示帮助：

`slurmdbd -h`

- 显示版本：

`slurmdbd -V`
