# wine reg add

> افزودن کلیدها و مقادیر جدید به رجیستری Wine.
> اطلاعات بیشتر: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>.

- افزودن کلید رجیستری جدید:

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}'`

- افزودن مقدار با دادهٔ مشخص زیر یک کلید:

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /d {{data}}`

- افزودن مقدار با نوع دادهٔ مشخص (پیش‌فرض `REG_SZ`):

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /t {{REG_SZ|REG_DWORD|REG_QWORD|REG_BINARY|REG_MULTI_SZ|REG_EXPAND_SZ|REG_NONE}} /d {{data}}`

- تنظیم مقدار پیش‌فرض (بدون نام) کلید:

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /ve /d {{data}}`

- افزودن مقدار `REG_MULTI_SZ` با تعیین نویسهٔ جداکنندهٔ رشته‌ها:

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /t REG_MULTI_SZ /s {{#}} /d '{{string1#string2#string3}}'`

- بازنویسی اجباری مقدار موجود بدون درخواست تأیید:

`wine reg add '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}} /d {{data}} /f`

- نمایش راهنما:

`wine reg add /?`
