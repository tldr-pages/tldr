# sbcast

> ارسال فایل به گره‌های تخصیص‌یافته به کار.
> این دستور فقط باید از داخل کار دسته‌ای Slurm استفاده شود.
> اطلاعات بیشتر: <https://slurm.schedmd.com/sbcast.html>.

- ارسال فایل به همهٔ گره‌های تخصیص‌یافته به کار فعلی:

`sbcast {{path/to/file}} {{path/to/destination}}`

- تشخیص خودکار کتابخانه‌های مشترک مورد نیاز فایل منتقل‌شده و انتقال آن‌ها نیز:

`sbcast --send-libs={{yes}} {{path/to/executable}} {{path/to/destination}}`
