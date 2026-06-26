# settings

> احصل على المزيد من المعلومات عن نظام اندرويد.
> لمزيد من التفاصيل: <https://web.archive.org/web/20240525010124/https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- قائمة الاعدادات في `global`:

`settings list global`

- احصل على قيمة اعدادات معينة:

`settings get {{global}} {{airplane_mode_on}}`

- حدد قيمة اعدادات محددة:

`settings put {{system}} {{screen_brightness}} {{42}}`

- احذف اعدادات معينة:

`settings delete {{secure}} {{screensaver_enabled}}`
