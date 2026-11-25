# lvchange

> تغییر ویژگی‌ها یا وضعیت فعال‌سازی حجم‌های منطقی.
> اطلاعات بیشتر: <https://manned.org/lvchange>.

- فعال کردن حجم منطقی:

`sudo lvchange {{[-a|--activate]}} y {{/dev/vg_name/lv_name}}`

- غیرفعال کردن حجم منطقی:

`sudo lvchange {{[-a|--activate]}} n {{/dev/vg_name/lv_name}}`

- فعال کردن فعال‌سازی خودکار برای حجم منطقی:

`sudo lvchange {{[-a|--activate]}} ay {{/dev/vg_name/lv_name}}`

- تنظیم حجم منطقی به حالت فقط‌خواندنی (برای خواندن و نوشتن از `rw` استفاده کنید):

`sudo lvchange {{[-p|--permission]}} r {{/dev/vg_name/lv_name}}`

- صرف‌نظر از فعال‌سازی حجم منطقی:

`sudo lvchange {{[-k|--setactivationskip]}} y {{/dev/vg_name/lv_name}}`

- تازه‌سازی حجم منطقی با جدیدترین فراداده:

`sudo lvchange --refresh {{/dev/vg_name/lv_name}}`
