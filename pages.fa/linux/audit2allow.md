# audit2allow

> تولید قواعد مجازسازی سیاست SELinux از گزارش‌های ممیزی.
> بخشی از بستهٔ `policycoreutils-python-utils` است.
> همچنین ببینید: `audit2why`, `ausearch`, `semodule`.
> اطلاعات بیشتر: <https://manned.org/audit2allow>.

- تولید و نمایش قواعد مجازسازی از موارد رد دسترسی اخیر در گزارش‌های ممیزی:

`sudo audit2allow {{[-a|--all]}}`

- تولید قواعد مجازسازی از یک فایل گزارش ممیزی مشخص:

`sudo audit2allow {{[-i|--input]}} {{path/to/audit.log}}`

- تولید یک ماژول سیاست از موارد رد دسترسی اخیر در گزارش‌های ممیزی:

`sudo audit2allow {{[-a|--all]}} {{[-M|--module]}} {{module_name}}`

- توضیح دلیل رخ دادن موارد رد دسترسی SELinux (مانند `audit2why`):

`sudo audit2allow {{[-a|--all]}} --why`

- نمایش اطلاعات مفصل دربارهٔ پیام‌های تولیدشده:

`sudo audit2allow {{[-a|--all]}} {{[-e|--explain]}}`

- استفاده از ماکروهای نصب‌شده برای تولید یک سیاست مرجع:

`sudo audit2allow {{[-a|--all]}} {{[-R|--reference]}}`

- تولید قواعد مجازسازی برای یک سرویس مشخص:

`sudo ausearch {{[-m|--message]}} avc {{[-c|--comm]}} {{service_name}} | audit2allow {{[-M|--module]}} {{policy_name}}`

- فعال کردن حالت خروجی مفصل:

`sudo audit2allow {{[-a|--all]}} {{[-v|--verbose]}}`
