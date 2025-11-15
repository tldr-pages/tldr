# sleep

> 延迟指定的一段时间。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html>.

- 按秒数延迟：

`sleep {{seconds}}`

- 延迟 [m]分钟（其他元素 [d]天，[h]小时，[s]秒，[inf]无穷 也可以使用）：

`sleep {{minutes}}m`

- 延迟 1 [d]天 3 [h]小时：

`sleep 1d 3h`

- 在 20 [m]分钟 延迟后执行指定命令：

`sleep 20m && {{command}}`
