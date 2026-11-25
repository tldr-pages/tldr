# exiqgrep

> اسکریپت Perl برای جست‌وجو با `grep` در خروجی صف Exim.
> اطلاعات بیشتر: <https://www.exim.org/exim-html-current/doc/html/spec_html/ch-exim_utilities.html>.

- تطبیق آدرس فرستنده با جست‌وجوی بدون حساسیت به بزرگی و کوچکی حروف:

`exiqgrep -f '<{{email@example.com}}>'`

- تطبیق آدرس فرستنده و نمایش فقط شناسهٔ پیام‌ها:

`exiqgrep -i -f '<{{email@example.com}}>'`

- تطبیق آدرس گیرنده با `-r`:

`exiqgrep -r '{{email@example.com}}'`

- حذف همهٔ پیام‌های مطابق با آدرس فرستنده از صف:

`exiqgrep -i -f '<{{email@example.com}}>' | xargs exim -Mrm`

- بررسی پیام‌های برگشت‌خورده:

`exiqgrep -f '^<>$'`

- نمایش تعداد پیام‌های برگشت‌خورده با `-c`:

`exiqgrep -c -f '^<>$'`
