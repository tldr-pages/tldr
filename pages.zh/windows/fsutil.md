# fsutil

> 显示有关文件系统卷的信息。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/fsutil>.

- 显示卷的列表：

`fsutil volume list`

- 显示卷的文件系统信息：

`fsutil fsInfo volumeInfo {{drive_letter|volume_path}}`

- 显示所有卷的文件系统自动修复的当前状态：

`fsutil repair state`

- 显示所有卷的脏位状态：

`fsutil dirty query`

- 设置卷的脏位状态：

`fsutil dirty set {{drive_letter|volume_path}}`