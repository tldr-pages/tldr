# stratis

> مدیریت استخرها و حجم‌های ذخیره‌سازی محلی با مدیر ذخیره‌سازی Stratis.
> حجم‌های Stratis از فایل‌سیستم XFS استفاده می‌کنند و به سرویس `stratisd` نیاز دارند.
> اطلاعات بیشتر: <https://stratis-storage.github.io/howto/>.

- شروع سرویس Stratis (باید پیش از مدیریت استخرها یا حجم‌ها فعال باشد):

`sudo systemctl start stratisd`

- ایجاد استخر ذخیره‌سازی از یک یا چند دستگاه:

`sudo stratis pool create {{pool_name}} {{/dev/sdX /dev/sdY ...}}`

- ایجاد فایل‌سیستم (حجم) در استخر:

`sudo stratis filesystem create {{pool_name}} {{volume_name}}`

- فهرست کردن همهٔ فایل‌سیستم‌های Stratis:

`sudo stratis filesystem list`

- قالب‌بندی و سوار کردن دستی حجم Stratis:

`sudo mkfs.xfs /dev/stratis/{{pool_name}}/{{volume_name}} && sudo mount /dev/stratis/{{pool_name}}/{{volume_name}} {{/mnt/target}}`

- افزودن حجم به `/etc/fstab` برای سوار شدن هنگام راه‌اندازی:

`echo /dev/stratis/{{pool_name}}/{{volume_name}} {{/mnt/target}} xfs defaults,x-systemd.requires=stratisd.service 0 0 | sudo tee {{[-a|--append]}} /etc/fstab`

- گسترش استخر موجود با افزودن دستگاه جدید:

`sudo stratis pool add-data {{pool_name}} {{/dev/sdZ}}`

- حذف حجم:

`sudo stratis filesystem destroy {{pool_name}} {{volume_name}}`
