# tmt try

> آزمایش سریع آزمون‌ها و محیط‌ها.
> اطلاعات بیشتر: <https://tmt.readthedocs.io/en/stable/stories/cli.html#try>.

- آزمایش سریع با روش فراهم‌سازی پیش‌فرض (بدون آزمون در دایرکتوری کاری فعلی):

`tmt try`

- اجرای آزمون در دایرکتوری کاری فعلی:

`cd {{path/to/test_directory}} && tmt try`

- استفاده از سیستم‌عامل مشخص:

`tmt try {{rhel-9}}`

- انتخاب تصویر و روش فراهم‌سازی دلخواه:

`tmt try {{fedora@container}}`

- انتخاب آزمون‌ها با فیلتر دلخواه:

`tmt try {{[-t|--test]}} {{feature}}`

- فراهم کردن مهمان و انتظار برای دستورها:

`tmt try {{[-a|--ask]}}`

- ورود مستقیم به مهمان بدون پرسش:

`tmt try {{[-l|--login]}}`

- نمایش راهنما:

`tmt try --help`
