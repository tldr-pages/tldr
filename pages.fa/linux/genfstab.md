# genfstab

> تولید خروجی مناسب برای افزودن به فایل `/etc/fstab`.
> اطلاعات بیشتر: <https://manned.org/genfstab>.

- تولید فایل `/etc/fstab` با UUID حجم‌ها هنگام نصب آرچ لینوکس (به دسترسی ریشه نیاز دارد):

`genfstab -U {{/mnt}} >>{{/mnt/etc/fstab}}`

- نمایش خروجی سازگار با fstab بر اساس برچسب حجم‌ها:

`genfstab -L {{path/to/mount_point}}`

- نمایش خروجی سازگار با fstab بر اساس UUID حجم‌ها:

`genfstab -U {{path/to/mount_point}}`

- نمایش خروجی سازگار با fstab بر اساس شناسهٔ مشخص:

`genfstab -t {{LABEL|UUID|PARTLABEL|PARTUUID}}`

- افزودن یک حجم به فایل `/etc/fstab` برای سوار شدن خودکار آن:

`genfstab -U {{path/to/mount_point}} | sudo tee -a /etc/fstab`
