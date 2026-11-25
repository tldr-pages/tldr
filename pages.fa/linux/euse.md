# euse

> فعال و غیرفعال کردن و دریافت اطلاعات پرچم‌های USE جنتو.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Euse>.

- فهرست کردن پرچم‌های سراسری فعال USE:

`euse {{[-a|--active]}} {{[-g|--global]}}`

- فهرست کردن پرچم‌های محلی فعال USE:

`euse {{[-a|--active]}} {{[-l|--local]}}`

- فعال کردن یک پرچم سراسری USE:

`sudo euse {{[-E|--enable]}} {{use_flag}}`

- غیرفعال کردن یک پرچم سراسری USE (قرار دادن علامت «-» پیش از پرچم USE):

`sudo euse {{[-D|--disable]}} {{use_flag}}`

- حذف یک پرچم سراسری USE:

`sudo euse {{[-P|--prune]}} {{use_flag}}`
