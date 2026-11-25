# tmt

> ابزار مدیریت آزمون برای ایجاد، اجرا و اشکال‌زدایی آزمون‌ها.
> برخی زیردستورها مانند `run` و `try` مستندات کاربرد جداگانه دارند.
> اطلاعات بیشتر: <https://tmt.readthedocs.io/en/stable/examples.html>.

- فهرست کردن آزمون‌ها، طرح‌ها و داستان‌های موجود:

`tmt`

- مقداردهی اولیهٔ فایل‌ها یا ساختار پروژهٔ tmt:

`tmt init`

- ایجاد آزمون جدید با قالب و پیوند:

`tmt test create {{[-t|--template]}} {{beakerlib}} --link {{verifies:issue#1234}}`

- فهرست کردن آزمون‌ها، طرح‌ها یا داستان‌های موجود:

`tmt {{test|plan|story}} ls {{pattern}}`

- نمایش فرادادهٔ مفصل آزمون در زمینهٔ مشخص:

`tmt {{[-c|--context]}} {{arch=aarch64}} test show`

- اعتبارسنجی فایل‌های tmt مطابق مشخصات:

`tmt lint`

- استفاده از فیلتر:

`tmt tests ls {{[-f|--filter]}} {{tag:foo}} {{[-f|--filter]}} {{tier:0}}`

- نمایش راهنما:

`tmt --help`
