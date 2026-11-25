# flatpak mask

> مستثنی کردن موارد از به‌روزرسانی و نصب خودکار.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-mask>.

- نادیده گرفتن به‌روزرسانی‌های یک Flatpak مشخص:

`flatpak mask {{com.example.app}}`

- لغو نادیده گرفتن به‌روزرسانی‌ها:

`flatpak mask --remove {{com.example.app}}`

- فهرست کردن همهٔ الگوهای مستثنی‌شدهٔ فعلی:

`flatpak mask {{--system|--user}}`
