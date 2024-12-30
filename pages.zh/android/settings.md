# 设置

> 获取关于Android操作系统的信息。
> 更多信息：<https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>。

- 列出`global`命名空间中的设置：

`settings list {{global}}`

- 获取特定设置的值：

`settings get {{global}} {{airplane_mode_on}}`

- 设置特定设置的值：

`settings put {{system}} {{screen_brightness}} {{42}}`

- 删除特定设置：

`settings delete {{secure}} {{screensaver_enabled}}`