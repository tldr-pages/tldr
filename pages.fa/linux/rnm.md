# rnm

> ابزار تغییر نام گروهی.
> اطلاعات بیشتر: <https://github.com/neurobin/rnm#basic-options>.

- جایگزینی رشتهٔ جست‌وجو با رشتهٔ جایگزین در نام فایل‌ها:

`rnm -ss {{old}} -rs {{new}} {{path/to/directory}}`

- استفاده از رشته‌های ثابت (لفظی) برای جست‌وجو و جایگزینی به‌جای `regex`:

`rnm -ssf {{old}} -rs {{new}} {{path/to/files}}`

- افزودن شاخص افزایشی خودکار به نام فایل‌ها از ۱:

`rnm -i 1 -inc 1 -rs {{_}} {{path/to/files}}`

- تغییر نام فایل‌ها با فهرست نام‌های جدید از فایل متنی:

`rnm -ns/f {{path/to/names.txt}} {{path/to/files}}`

- تغییر نام فقط فایل‌ها (نادیده گرفتن دایرکتوری‌ها و پیوندها):

`rnm -fo -ss {{pattern}} -rs {{replacement}} {{path/to/files}}`

- مرتب‌سازی فایل‌های ورودی بر اساس زمان تغییر پیش از تغییر نام:

`rnm -s/mt -ss {{pattern}} -rs {{replacement}} {{path/to/files}}`

- اجرای شبیه‌سازی بدون اعمال تغییرات واقعی:

`rnm -sim -ss {{pattern}} -rs {{replacement}} {{path/to/files}}`

- واگرد آخرین عملیات تغییر نام:

`rnm -u`
