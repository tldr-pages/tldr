# dex

> برنامهٔ DesktopEntry Execution برای تولید و اجرای فایل‌های DesktopEntry از نوع Application.
> اطلاعات بیشتر: <https://github.com/jceb/dex#dex>.

- اجرای همهٔ برنامه‌ها در پوشه‌های شروع خودکار:

`dex {{[-a|--autostart]}}`

- اجرای همهٔ برنامه‌ها در پوشه‌های مشخص:

`dex {{[-a|--autostart]}} {{[-s|--search-paths]}} {{path/to/directory1}}:{{path/to/directory2}}:{{path/to/directory3}}:`

- پیش‌نمایش برنامه‌هایی که در شروع خودکار مخصوص GNOME اجرا می‌شوند:

`dex {{[-a|--autostart]}} {{[-e|--environment]}} {{GNOME}}`

- شبیه‌سازی شروع خودکار معمول و نمایش برنامه‌هایی که اجرا خواهند شد:

`dex {{[-a|--autostart]}} {{[-d|--dry-run]}}`

- پیش‌نمایش مقدار ویژگی `Name` در DesktopEntry:

`dex {{[-p|--property]}} {{Name}} {{path/to/file.desktop}}`

- ایجاد یک DesktopEntry برای برنامه‌ای در دایرکتوری فعلی:

`dex {{[-c|--create]}} {{path/to/file.desktop}}`

- اجرای یک برنامهٔ واحد در پایانهٔ مشخص (با `Terminal=true` در فایل `.desktop`):

`dex --term {{terminal}} {{path/to/file.desktop}}`
