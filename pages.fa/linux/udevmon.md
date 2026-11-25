# udevmon

> دریافت و پایش دستگاه‌های ورودی برای شروع وظایف.
> رویدادها را مطابق فایل‌های پیکربندی فیلتر یا تغییر می‌دهد (پیش‌فرض: `/etc/interception/udevmon.d/*.yaml`).
> اطلاعات بیشتر: <https://gitlab.com/interception/linux/tools/-/tree/master#udevmon>.

- شروع udevmon با فایل پیکربندی مشخص:

`udevmon -c {{path/to/config.yaml}}`
