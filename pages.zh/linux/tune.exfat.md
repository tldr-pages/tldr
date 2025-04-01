# tune.exfat

> 调整 exFAT 文件系统的可调参数。
> 更多信息：<https://manned.org/tune.exfat>.

- 打印文件系统的卷标：

`tune.exfat {{[-l|--print-label]}} {{/dev/sdXY}}`

- 设置文件系统的卷标：

`tune.exfat {{[-L|--set-label]}} {{new_label}} {{/dev/sdXY}}`

- 打印文件系统的卷 GUID：

`tune.exfat {{[-u|--print-guid]}} {{/dev/sdXY}}`

- 设置文件系统的卷 GUID：

`tune.exfat {{[-U|--set-guid]}} {{new_guid}} {{/dev/sdXY}}`

- 打印文件系统的卷序列号：

`tune.exfat {{[-i|--print-serial]}} {{/dev/sdXY}}`

- 设置文件系统的卷序列号：

`tune.exfat {{[-I|--set-serial]}} {{new_serial}} {{/dev/sdXY}}`