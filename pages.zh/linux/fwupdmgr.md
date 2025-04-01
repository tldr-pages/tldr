# fwupdmgr

> 更新设备固件，包括 UEFI，使用 `fwupd`。
> 更多信息：<https://fwupd.org/>。

- 显示 fwupd 检测到的所有设备：

`fwupdmgr get-devices`

- 从 LVFS 下载最新的固件元数据：

`fwupdmgr refresh`

- 列出系统上设备可用的更新：

`fwupdmgr get-updates`

- 安装固件更新：

`fwupdmgr update`