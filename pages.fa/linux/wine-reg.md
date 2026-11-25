# wine reg

> مدیریت کلیدها و مقادیر آن‌ها در رجیستری Wine.
> برخی زیردستورها مانند `add`، `delete` و `query` مستندات کاربرد جداگانه دارند.
> اطلاعات بیشتر: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- افزودن یا بازنویسی مقدار زیر کلید (و ساخت کلید در صورت نیاز):

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /d {{data}} /f`

- نمایش مقادیر ذخیره‌شده زیر کلید:

`wine reg query '{{HKEY_CURRENT_USER\path\to\key}}'`

- حذف مقدار از کلید:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /f`

- کپی کلید و همهٔ زیرکلیدهای آن به محل جدید:

`wine reg copy '{{HKEY_CURRENT_USER\path\to\source_key}}' '{{HKEY_CURRENT_USER\path\to\destination_key}}' /s`

- صادرات کلید و زیرکلیدهای آن به فایل `.reg`:

`wine reg export '{{HKEY_CURRENT_USER\path\to\key}}' {{path/to/file.reg}}`

- وارد کردن مدخل‌های رجیستری از فایل `.reg`:

`wine reg import {{path/to/file.reg}}`

- نمایش راهنما:

`wine reg /?`
