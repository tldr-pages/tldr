# ip rule

> مدیریت پایگاه دادهٔ سیاست مسیریابی IP.
> همچنین ببینید: `ip route`.
> اطلاعات بیشتر: <https://manned.org/ip-rule>.

- نمایش سیاست مسیریابی:

`ip {{[ru|rule]}}`

- ایجاد قانون مسیریابی عمومی جدید با اولویت بالاتر از `main`:

`sudo ip {{[ru|rule]}} {{[a|add]}} from all lookup {{table_id}}`

- افزودن قانون جدید بر اساس آدرس مبدأ بسته‌ها:

`sudo ip {{[ru|rule]}} {{[a|add]}} from {{192.168.178.2/32}} lookup {{table_id}}`

- افزودن قانون جدید بر اساس آدرس مقصد بسته‌ها:

`sudo ip {{[ru|rule]}} {{[a|add]}} to {{192.168.178.2/32}} lookup {{table_id}}`

- حذف قانون بر اساس آدرس مبدأ بسته‌ها:

`sudo ip {{[ru|rule]}} {{[d|delete]}} from {{192.168.178.2/32}}`

- حذف همهٔ قوانین مسیریابی:

`sudo ip {{[ru|rule]}} {{[f|flush]}}`

- ذخیرهٔ همهٔ قوانین در فایل:

`ip {{[ru|rule]}} {{[s|save]}} >{{path/to/ip_rules.dat}}`

- بازیابی همهٔ قوانین از فایل:

`sudo ip <{{path/to/ip_rules.dat}} {{[ru|rule]}} {{[r|restore]}}`
