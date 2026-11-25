# look

> نمایش خطوطی از فایل که با پیشوند مشخص آغاز می‌شوند.
> توجه: خطوط فایل باید مرتب شده باشند.
> همچنین : `grep`, `sort`.
> اطلاعات بیشتر: <https://manned.org/look>.

- جست‌وجوی خطوط آغازشونده با پیشوند مشخص در فایل مشخص:

`look {{prefix}} {{path/to/file}}`

- جست‌وجوی بدون حساسیت به بزرگی و کوچکی حروف فقط در نویسه‌های فاصله و الفبایی‌عددی:

`look {{[-f|--ignore-case]}} {{[-d|--alphanum]}} {{prefix}} {{path/to/file}}`

- تعیین نویسهٔ پایان رشته (پیش‌فرض فاصله است):

`look {{[-t|--terminate]}} {{,}}`

- جست‌وجو در `/usr/share/dict/words` (گزینه‌های `--ignore-case` و `--alphanum` فرض می‌شوند):

`look {{prefix}}`

- جست‌وجو در `/usr/share/dict/web2` (گزینه‌های `--ignore-case` و `--alphanum` فرض می‌شوند):

`look {{[-a|--alternative]}} {{prefix}}`
