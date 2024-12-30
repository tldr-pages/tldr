# atq

> 显示通过 `at` 或 `batch` 命令调度的作业。
> 更多信息：<https://manned.org/atq>。

- 显示当前用户的调度作业：

`atq`

- 显示来自 'a' [q]ueue 的作业（队列有单字符名称）：

`atq -q {{a}}`

- 显示所有用户的作业（以超级用户身份运行）：

`sudo atq`