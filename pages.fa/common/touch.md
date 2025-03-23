# touch

> ایجاد فایل‌ها و تنظیم زمان‌های دسترسی/تغییر.
> اطلاعات بیشتر: <https://manned.org/touch>.

- ایجاد فایل‌های مشخص:

`touch {{path/to/file1 path/to/file2 ...}}`

- تنظیم زمان [a]دسترسی یا [m]تغییر فایل به زمان فعلی و عدم [c]ایجاد فایل در صورت عدم وجود:

`touch {{[-c|--no-create]}} -{{a|m}} {{path/to/file1 path/to/file2 ...}}`

- تنظیم [t]زمان فایل به یک مقدار مشخص و عدم [c]ایجاد فایل در صورت عدم وجود:

`touch {{[-c|--no-create]}} -t {{YYYYMMDDHHMM.SS}} {{path/to/file1 path/to/file2 ...}}`

- تنظیم زمان فایل‌ها به زمان فایل [r]مرجع، و عدم [c]ایجاد فایل در صورت عدم وجود:

`touch {{[-c|--no-create]}} {{[-r|--reference]}} {{path/to/reference_file}} {{path/to/file1 path/to/file2 ...}}`
