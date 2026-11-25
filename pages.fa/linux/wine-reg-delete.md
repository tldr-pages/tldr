# wine reg delete

> حذف کلیدها و مقادیر از رجیستری Wine.
> اطلاعات بیشتر: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- حذف کلید رجیستری و همهٔ مقادیر آن:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}'`

- حذف مقدار مشخص زیر کلید:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}}`

- حذف مقدار پیش‌فرض (بدون نام) کلید:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}' /ve`

- حذف همهٔ مقادیر زیر کلید بدون حذف خود کلید:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}' /va`

- حذف اجباری بدون درخواست تأیید:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}' /f`

- نمایش راهنما:

`wine reg delete /?`
