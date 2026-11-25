# df

> نمایش نمای کلی استفاده از فضای دیسک سیستم فایل.
> همچنین : `ncdu`, `duf`.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>.

- نمایش همهٔ سیستم‌های فایل و میزان استفادهٔ آن‌ها از دیسک:

`df`

- نمایش همهٔ سیستم‌های فایل در قالب خوانا:

`df {{[-h|--human-readable]}}`

- نمایش سیستم فایل حاوی فایل یا دایرکتوری مشخص:

`df {{path/to/file_or_directory}}`

- گنجاندن آمار تعداد inodeهای آزاد:

`df {{[-i|--inodes]}}`

- نمایش سیستم‌های فایل به‌جز انواع مشخص‌شده:

`df {{[-x|--exclude-type]}} {{squashfs}} {{[-x|--exclude-type]}} {{tmpfs}}`

- نمایش انواع سیستم فایل:

`df {{[-T|--print-type]}}`
