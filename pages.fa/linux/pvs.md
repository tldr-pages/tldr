# pvs

> نمایش اطلاعات حجم‌های فیزیکی.
> همچنین : `lvm`.
> اطلاعات بیشتر: <https://manned.org/pvs>.

- نمایش اطلاعات حجم‌های فیزیکی:

`sudo pvs`

- نمایش حجم‌های غیرفیزیکی:

`sudo pvs {{[-a|--all]}}`

- تغییر نمایش پیش‌فرض برای نمایش جزئیات بیشتر:

`sudo pvs {{[-v|--verbose]}}`

- نمایش فقط فیلدهای مشخص:

`sudo pvs {{[-o|--options]}} {{field_name_1,field_name_2,...}}`

- افزودن فیلد به نمایش پیش‌فرض:

`sudo pvs {{[-o|--options]}} +{{field_name}}`

- عدم نمایش خط سربرگ:

`sudo pvs --noheadings`

- استفاده از جداکننده برای جداسازی فیلدها:

`sudo pvs --separator {{special_character}}`
