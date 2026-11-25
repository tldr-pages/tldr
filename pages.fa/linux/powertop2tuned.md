# powertop2tuned

> ایجاد پروفایل‌های TuneD از پیشنهادهای PowerTOP.
> بخشی از `tuned-utils` است.
> همچنین : `powertop`, `tuned-adm`.
> اطلاعات بیشتر: <https://docs.fedoraproject.org/en-US/quick-docs/automatic-power-management-power2top/>.

- ایجاد پروفایل جدید TuneD بر اساس پیشنهادهای فعلی PowerTOP:

`sudo powertop2tuned {{profile_name}}`

- ایجاد پروفایل جدید و فعال کردن خودکار بیشتر پیشنهادها:

`sudo powertop2tuned {{[-e|--enable]}} {{profile_name}}`

- ایجاد پروفایل از گزارش HTML موجود PowerTOP:

`sudo powertop2tuned {{[-i|--input]}} {{path/to/report.html}} {{profile_name}}`

- ایجاد پروفایل جدید در دایرکتوری مشخص:

`sudo powertop2tuned {{[-o|--output]}} {{path/to/directory}} {{profile_name}}`

- ایجاد پروفایل جدید بدون ادغام پروفایل فعال:

`sudo powertop2tuned {{[-n|--new-profile]}} {{profile_name}}`

- ادغام پیشنهادها با پروفایل موجود مشخص:

`sudo powertop2tuned {{[-m|--merge-profile]}} {{existing_profile}} {{profile_name}}`

- بازنویسی اجباری دایرکتوری پروفایل موجود:

`sudo powertop2tuned {{[-f|--force]}} {{profile_name}}`
