# wine reg copy

> کپی کلید رجیستری به محل جدید در رجیستری Wine.
> اطلاعات بیشتر: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-copy>.

- کپی کلید رجیستری به محل جدید:

`wine reg copy '{{HKEY_CURRENT_USER\path\to\source_key}}' '{{HKEY_CURRENT_USER\path\to\destination_key}}'`

- کپی بازگشتی کلید همراه همهٔ زیرکلیدها و مقادیر آن:

`wine reg copy '{{HKEY_CURRENT_USER\path\to\source_key}}' '{{HKEY_CURRENT_USER\path\to\destination_key}}' /s`

- بازنویسی اجباری مقصد بدون درخواست تأیید:

`wine reg copy '{{HKEY_CURRENT_USER\path\to\source_key}}' '{{HKEY_CURRENT_USER\path\to\destination_key}}' /f`

- کپی بازگشتی و اجباری کلید با بازنویسی مقصد:

`wine reg copy '{{HKEY_CURRENT_USER\path\to\source_key}}' '{{HKEY_CURRENT_USER\path\to\destination_key}}' /s /f`

- نمایش راهنما:

`wine reg copy /?`
