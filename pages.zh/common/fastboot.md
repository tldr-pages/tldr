# fastboot

> 在引导加载程序模式下与连接的Android设备通信（ADB无法工作的唯一地方）。
> 更多信息：<https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>。

- 解锁引导加载程序：

`fastboot oem unlock`

- 重新锁定引导加载程序：

`fastboot oem lock`

- 从fastboot模式重启设备到fastboot模式：

`fastboot reboot bootloader`

- 刷写指定的镜像：

`fastboot flash {{path/to/file.img}}`

- 刷写自定义恢复镜像：

`fastboot flash recovery {{path/to/file.img}}`

- 列出连接的设备：

`fastboot devices`

- 显示设备的所有信息：

`fastboot getvar all`