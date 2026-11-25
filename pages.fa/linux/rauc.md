# rauc

> کارخواه سبک به‌روزرسانی برای دستگاه‌های لینوکس تعبیه‌شده جهت ایجاد، بررسی و نصب بسته‌های به‌روزرسانی.
> اطلاعات بیشتر: <https://manned.org/rauc>.

- نمایش وضعیت فعلی سیستم و نمای کلی slotها:

`rauc status`

- نصب بستهٔ به‌روزرسانی:

`rauc install {{path/to/bundle.raucb|https://example.com/bundle.raucb}}`

- نمایش اطلاعات بستهٔ به‌روزرسانی مشخص:

`rauc info {{path/to/bundle.raucb}}`

- ایجاد بستهٔ به‌روزرسانی امضاشده از دایرکتوری:

`rauc bundle --cert {{path/to/cert.pem}} --key {{path/to/key.pem}} {{path/to/input_dir}} {{path/to/output.raucb}}`

- استخراج محتویات بستهٔ به‌روزرسانی:

`rauc extract {{path/to/bundle.raucb}} {{path/to/output_directory}}`

- علامت‌گذاری slot راه‌اندازی‌شدهٔ فعلی به‌عنوان سالم برای تأیید موفقیت به‌روزرسانی:

`rauc status mark-good`

- علامت‌گذاری slot مشخص به‌عنوان خراب برای جلوگیری از راه‌اندازی آن:

`rauc status mark-bad {{slot_name}}`

- تغییر slot فعال راه‌اندازی به slot دیگر موجود:

`rauc status mark-active other`
