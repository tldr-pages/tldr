# ventoy

> ابزاری برای ایجاد درایوهای USB قابل راه‌اندازی با فایل‌های ISO.
> اطلاعات بیشتر: <https://www.ventoy.net/en/doc_start.html#doc_linux_cli>.

- نصب Ventoy روی درایو مشخص با پیش‌فرض‌ها:

`sudo ventoy -i {{/dev/sdX}}`

- نصب Ventoy با سبک پارتیشن GPT به‌جای MBR:

`sudo ventoy -i -g {{/dev/sdX}}`

- نصب Ventoy با سبک GPT و برچسب پارتیشن دلخواه و Secure Boot غیرفعال:

`sudo ventoy -i -g -S -L {{LABEL_NAME}} {{/dev/sdX}}`

- نصب Ventoy و رزرو فضا در انتهای دیسک:

`sudo ventoy -i -r {{SIZE_MB}} {{/dev/sdX}}`

- نصب اجباری Ventoy (نصب موجود را بازنویسی می‌کند):

`sudo ventoy -I {{/dev/sdX}}`

- به‌روزرسانی Ventoy روی درایو:

`sudo ventoy -u {{/dev/sdX}}`

- نمایش اطلاعات Ventoy برای درایو:

`sudo ventoy -l {{/dev/sdX}}`

- تلاش برای نصب غیرویرانگر در صورت امکان (Ventoy دیسک را مجدداً قالب‌بندی نمی‌کند):

`sudo ventoy -i -n {{/dev/sdX}}`
