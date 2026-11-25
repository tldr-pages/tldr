# wine

> اجرای فایل‌های اجرایی Windows در سیستم‌های مبتنی بر Unix.
> اطلاعات بیشتر: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- اجرای برنامهٔ مشخص در محیط `wine`:

`wine {{command}}`

- اجرای برنامهٔ مشخص در پس‌زمینه:

`wine start {{command}}`

- نصب یا حذف بستهٔ MSI:

`wine msiexec /{{i|x}} {{path/to/package.msi}}`

- اجرای `File Explorer`، `Notepad` یا `WordPad`:

`wine {{explorer|notepad|write}}`

- اجرای `Registry Editor`، `Control Panel` یا `Task Manager`:

`wine {{regedit|control|taskmgr}}`

- باز کردن دسکتاپ مجازی Wine:

`wine explorer /desktop={{shell}},{{1920x1080}}`

- اجرای ابزار پیکربندی:

`wine winecfg`

- افزودن کلید رجیستری:

`wine reg add '{{path\to\registry_key}}' /v {{Value_name}} /t {{REG_SZ|REG_BINARY|REG_DWORD|...}} /d '{{data}}'`
