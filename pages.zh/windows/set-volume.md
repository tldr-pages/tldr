# Set-Volume

> 设置或更改现有卷的文件系统标签。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/storage/set-volume>.

- 更改由驱动器字母标识的卷的文件系统标签：

`Set-Volume -DriveLetter "D" -NewFileSystemLabel "DataVolume"`

- 更改由系统标签标识的卷的文件系统标签：

`Set-Volume -FileSystemLabel "OldLabel" -NewFileSystemLabel "NewLabel"`

- 使用卷对象修改卷的属性：

`Set-Volume -InputObject $(Get-Volume -DriveLetter "E") -NewFileSystemLabel "Backup"`

- 为卷指定数据去重模式：

`Set-Volume -DriveLetter "D" -DedupMode Backup`