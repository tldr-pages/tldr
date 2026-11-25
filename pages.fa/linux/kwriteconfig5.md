# kwriteconfig5

> نوشتن ورودی‌های KConfig برای KDE Plasma.
> اطلاعات بیشتر: <https://userbase.kde.org/KDE_System_Administration/Configuration_Files>.

- تنظیم کلید پیکربندی سراسری:

`kwriteconfig5 --group {{group_name}} --key {{key}} {{value}}`

- تنظیم کلید در فایل پیکربندی مشخص:

`kwriteconfig5 --file {{path/to/file}} --group {{group_name}} --key {{key}} {{value}}`

- حذف کلید:

`kwriteconfig5 --group {{group_name}} --key {{key}} --delete`

- استفاده از systemd برای شروع نشست Plasma در صورت وجود:

`kwriteconfig5 --file {{startkderc}} --group {{General}} --key systemdBoot {{true}}`

- پنهان کردن نوار عنوان هنگام بیشینه بودن پنجره (مانند Ubuntu):

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{Windows}} --key {{BorderlessMaximizedWindows}} {{true}}`

- پیکربندی KRunner برای باز شدن با میانبر سراسری Meta (Command/Windows):

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{ModifierOnlyShortcuts}} --key {{Meta}} "{{org.kde.kglobalaccel,/component/krunner_desktop,org.kde.kglobalaccel.Component,invokeShortcut,_launch}}"`

- نمایش راهنما:

`kwriteconfig5 --help`
