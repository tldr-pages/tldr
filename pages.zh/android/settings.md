# settings

> 获取关于 Android OS 的信息。
> 更多信息：<https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- 在 `全局` 命名空间中显示环境变量列表：

`settings list {{global}}`

- 获取指定环境变量的值：

`settings get {{global}} {{airplane_mode_on}}`

- 设置指定环境变量的值：

`settings put {{system}} {{screen_brightness}} {{42}}`

- 删除指定环境变量：

`settings delete {{secure}} {{screensaver_enabled}}`
