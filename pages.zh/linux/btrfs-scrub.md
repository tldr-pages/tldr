# btrfs scrub

> 清理 btrfs 文件系统以验证数据完整性。
> 建议每月运行一次 scrub.
> 更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- 开始 scrub：

`sudo btrfs scrub start {{指向挂载点的路径}}`

- 显示正在进行或上次完成的 scrub 的状态：

`sudo btrfs scrub status {{指向挂载点的路径}}`

- 取消正在进行的 scrub：

`sudo btrfs scrub cancel {{指向挂载点的路径}}`

- 恢复先前取消的 scrub：

`sudo btrfs scrub resume {{指向挂载点的路径}}`

- 开始擦洗，但要等到 scrub 完成后才能退出：

`sudo btrfs scrub start -B {{指向挂载点的路径}}`

- 在安静模式下启动 scrub（不打印错误或统计信息）：

`sudo btrfs scrub start -q {{指向挂载点的路径}}`
