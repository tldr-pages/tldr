# ppa-purge

> غیرفعال کردن PPA و بازگرداندن بسته‌های آن به نسخه‌های رسمی.
> اطلاعات بیشتر: <https://manned.org/ppa-purge>.

- غیرفعال کردن PPA و تنزل بسته‌های آن به نسخه‌های رسمی:

`sudo ppa-purge ppa:{{owner}}/{{ppa_name}}`

- غیرفعال کردن PPA فقط با تعیین مالک آن (نام پیش‌فرض PPA برابر `ppa` است):

`sudo ppa-purge -o {{owner}}`

- غیرفعال کردن PPA با تعیین مالک و نام PPA:

`sudo ppa-purge -o {{owner}} -p {{ppa_name}}`

- پاسخ «بله» به همهٔ پرسش‌های مدیر بسته:

`sudo ppa-purge -y ppa:{{owner}}/{{ppa_name}}`

- استفاده از توزیع مشخص به‌جای توزیع شناسایی‌شده:

`sudo ppa-purge -d {{distribution}} ppa:{{owner}}/{{ppa_name}}`

- نمایش راهنما:

`ppa-purge -h`
