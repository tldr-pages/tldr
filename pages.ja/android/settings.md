# settings

> Android OSに関連する情報を取得します。
> もっと詳しく: <https://web.archive.org/web/20240525010124/https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>。

- `global` 名前空間にある設定を表示します:

`settings list {{global}}`

- 指定した設定値を取得します:

`settings get {{global}} {{airplane_mode_on}}`

- 指定した設定値を設定します:

`settings put {{system}} {{screen_brightness}} {{42}}`

- 指定した設定を削除します:

`settings delete {{secure}} {{screensaver_enabled}}`
