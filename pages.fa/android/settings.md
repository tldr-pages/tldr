# settings

> دریافت اطلاعات مربوط به سیستم عامل اندروید.
> اطلاعات بیشتر: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- نمایش یک فهرست از تنظیمات داخل فضای نام `global` :

`settings list {{global}}`

- دریافت مقدار یک تنظیم مشخص :

`settings get {{global}} {{airplane_mode_on}}`

- انتصاب یک مقدار مشخص به یک تنظیم :

`settings put {{system}} {{screen_brightness}} {{42}}`

- حذف یک تنظیم مشخص :

`settings delete {{secure}} {{screensaver_enabled}}`
