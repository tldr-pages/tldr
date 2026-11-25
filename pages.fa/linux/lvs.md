# lvs

> نمایش اطلاعات حجم‌های منطقی.
> همچنین : `lvm`.
> اطلاعات بیشتر: <https://manned.org/lvs>.

- نمایش اطلاعات حجم‌های منطقی:

`sudo lvs`

- نمایش همهٔ حجم‌های منطقی:

`sudo lvs {{[-a|--all]}}`

- تغییر نمایش پیش‌فرض برای نمایش جزئیات بیشتر:

`sudo lvs {{[-v|--verbose]}}`

- نمایش فقط فیلدهای مشخص:

`sudo lvs {{[-o|--options]}} {{field_name_1,field_name_2,...}}`

- افزودن فیلد به نمایش پیش‌فرض:

`sudo lvs {{[-o|--options]}} +{{field_name}}`

- عدم نمایش خط سربرگ:

`sudo lvs --noheadings`

- استفاده از جداکننده برای جداسازی فیلدها:

`sudo lvs --separator {{=}}`
