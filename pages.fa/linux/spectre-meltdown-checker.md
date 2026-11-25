# spectre-meltdown-checker

> ابزار تشخیص اقدامات کاهشی Spectre و Meltdown.
> اطلاعات بیشتر: <https://manned.org/spectre-meltdown-checker>.

- بررسی هستهٔ در حال اجرا برای Spectre یا Meltdown:

`sudo spectre-meltdown-checker`

- بررسی هستهٔ در حال اجرا و نمایش توضیح اقدامات لازم برای کاهش آسیب‌پذیری:

`sudo spectre-meltdown-checker --explain`

- بررسی گونه‌های مشخص (پیش‌فرض همه):

`sudo spectre-meltdown-checker --variant {{1|2|3|3a|4|l1tf|msbds|mfbds|mlpds|mdsum|taa|mcespc|srbds}}`

- نمایش خروجی در قالب مشخص:

`sudo spectre-meltdown-checker --batch {{text|json|nrpe|prometheus|short}}`

- استفاده نکردن از رابط `/sys` حتی در صورت وجود:

`sudo spectre-meltdown-checker --no-sysfs`

- بررسی هسته‌ای که در حال اجرا نیست:

`sudo spectre-meltdown-checker --kernel {{path/to/kernel_file}}`
