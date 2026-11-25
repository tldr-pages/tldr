# wine reg query

> نمایش کلیدها، مقادیر و داده‌ها در رجیستری Wine.
> اطلاعات بیشتر: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- نمایش همهٔ مقادیر مستقیماً زیر یک کلید:

`wine reg query '{{HKEY_CURRENT_USER\path\to\key}}'`

- نمایش مقدار مشخص کلید:

`wine reg query '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}}`

- نمایش مقدار پیش‌فرض (بدون نام) کلید:

`wine reg query '{{HKEY_CURRENT_USER\path\to\key}}' /ve`

- نمایش بازگشتی کلید همراه همهٔ زیرکلیدها و مقادیر آن:

`wine reg query '{{HKEY_CURRENT_USER\path\to\key}}' /s`

- نمایش راهنما:

`wine reg query /?`
