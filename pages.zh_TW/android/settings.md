# settings

> 獲取關於 Android OS 的資訊。
> 更多資訊：<https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- 在 `global` 命名空間中顯示環境變數列表：

`settings list {{global}}`

- 獲取指定環境變數的值：

`settings get {{global}} {{airplane_mode_on}}`

- 設定指定環境變數的值：

`settings put {{system}} {{screen_brightness}} {{42}}`

- 刪除指定環境變數：

`settings delete {{secure}} {{screensaver_enabled}}`
