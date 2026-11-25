# foreman

> مدیریت برنامه‌های مبتنی بر Procfile.
> اطلاعات بیشتر: <https://manned.org/foreman>.

- شروع یک برنامه با Procfile موجود در دایرکتوری فعلی:

`foreman start`

- شروع یک برنامه با Procfile مشخص:

`foreman start {{[-f|--procfile]}} {{Procfile}}`

- شروع یک برنامهٔ مشخص:

`foreman start {{process}}`

- اعتبارسنجی قالب Procfile:

`foreman check`

- اجرای دستورهای یک‌باره با محیط فرایند:

`foreman run {{command}}`

- شروع همهٔ فرایندها به‌جز فرایند با نام «worker»:

`foreman start {{[-m|--formation]}} all=1,{{worker}}=0`
