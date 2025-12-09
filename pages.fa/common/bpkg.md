# bpkg

> یک پکیج منیجر برای بش اسکریپت.
> اطلاعات بیشتر: <https://github.com/bpkg/bpkg>.

- بروزرسانی فهرست محلی:

`bpkg update`

- نصب یک بسته به صورت گلوبال:

`bpkg install --global {{package}}`

- نصب یک بسته در یک زیرپوشه در پوشه ی کنونی:

`bpkg install {{package}}`

- نصب یک نسخه خاص از یک بسته به صورت گلوبال:

`bpkg install {{package}}@{{version}} -g`

- نمایش جزئیات یک بسته خاص:

`bpkg show {{package}}`

- اجرای یک دستور، آرگومان ها به صورت اختیاری نوشته شده اند:

`bpkg run {{command}} {{argument1 argument2 ...}}`
