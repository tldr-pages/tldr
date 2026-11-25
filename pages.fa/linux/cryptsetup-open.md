# cryptsetup open

> ایجاد یک نگاشت رمزگشایی‌شده از یک حجم رمزگذاری‌شده.
> توجه: فعال کردن TRIM ممکن است مقدار کمی اطلاعات را افشا کند (بلوک‌های آزادشده و احتمالاً نوع سیستم فایل)، اما همچنان توصیه می‌شود زیرا داده‌ها امن می‌مانند و SSDهای بدون TRIM سریع‌تر مستهلک می‌شوند.
> اطلاعات بیشتر: <https://manned.org/cryptsetup-open>.

- باز کردن یک حجم LUKS و ایجاد نگاشت رمزگشایی‌شده در `/dev/mapper/mapping_name`:

`cryptsetup open {{/dev/sdXY}} {{mapping_name}}`

- استفاده از فایل کلید به جای عبارت عبور:

`cryptsetup open {{[-k|--key-file]}} {{path/to/file}} {{/dev/sdXY}} {{mapping_name}}`

- مجاز کردن استفاده از TRIM روی دستگاه:

`cryptsetup open --allow-discards {{/dev/sdXY}} {{mapping_name}}`

- نوشتن گزینهٔ `--allow-discards` در سربرگ LUKS (پس از آن هنگام باز کردن دستگاه همیشه استفاده می‌شود):

`cryptsetup open --allow-discards --persistent {{/dev/sdXY}} {{mapping_name}}`

- باز کردن یک حجم LUKS و فقط‌خواندنی کردن نگاشت رمزگشایی‌شده:

`cryptsetup open {{[-r|--readonly]}} {{/dev/sdXY}} {{mapping_name}}`
