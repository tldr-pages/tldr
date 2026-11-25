# vgs

> نمایش اطلاعات گروه‌های حجم.
> همچنین ببینید: `lvm`.
> اطلاعات بیشتر: <https://manned.org/vgs>.

- نمایش اطلاعات گروه‌های حجم:

`sudo vgs`

- نمایش همهٔ گروه‌های حجم:

`sudo vgs {{[-a|--all]}}`

- تغییر نمایش پیش‌فرض برای نمایش جزئیات بیشتر:

`sudo vgs {{[-v|--verbose]}}`

- نمایش فقط فیلدهای مشخص:

`sudo vgs {{[-o|--options]}} {{field_name_1,field_name_2,...}}`

- افزودن فیلد به نمایش پیش‌فرض:

`sudo vgs {{[-o|--options]}} +{{field_name}}`

- عدم نمایش خط سربرگ:

`sudo vgs --noheadings`

- استفاده از جداکننده برای جداسازی فیلدها:

`sudo vgs --separator =`
