# 睡眠

> 延迟指定的时间。
> 更多信息：<https://www.gnu.org/software/coreutils/sleep>。

- 以秒为单位的延迟：

`sleep {{秒数}}`

- 以[m]分钟为单位的延迟。（其他单位[d]天、[h]小时、[s]秒、[inf]无穷大也可以使用）：

`sleep {{分钟}}m`

- 延迟1[d]天3[h]小时：

`sleep 1d 3h`

- 在20[m]分钟延迟后执行特定命令：

`sleep 20m && {{命令}}`