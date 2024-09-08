# fastboot

> 在引导加载程序模式下与连接的 Android 设备通信（在这里无法使用 ADB）。
> 更多信息：<https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>.

- 解锁引导加载程序：

`fastboot oem unlock`

- 回锁引导加载程序：

`fastboot oem lock`

- 从 fastboot 模式再次重启到 fastboot 模式：

`fastboot reboot bootloader`

- 刷入镜像：

`fastboot flash {{路径/到/文件.img}}`

- 刷入自定义恢复镜像：

`fastboot flash recovery {{路径/到/文件.img}}`

- 列出已连接的设备：

`fastboot devices`

- 列出设备所有信息：

`fastboot getvar all`
