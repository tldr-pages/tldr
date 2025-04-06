# git count-objects

> 统计未打包对象数量及其磁盘占用情况。
> 更多信息：<https://git-scm.com/docs/git-count-objects>.

- 统计所有对象并显示总磁盘使用量：

`git count-objects`

- 统计所有对象并以易读格式显示总磁盘使用量（如KB/MB）：

`git count-objects --human-readable`

- 显示详细统计信息（包括对象类型细分）：

`git count-objects --verbose`

- 以易读格式显示详细统计信息：

`git count-objects --human-readable --verbose`
