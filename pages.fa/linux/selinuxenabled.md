# selinuxenabled

> بررسی فعال بودن SELinux.
> اگر SELinux فعال باشد کد خروج ۰ و در غیر این صورت ۱ برمی‌گرداند.
> همچنین ببینید: `getenforce`, `setenforce`, `sestatus`.
> اطلاعات بیشتر: <https://manned.org/selinuxenabled>.

- بررسی فعال بودن SELinux (بدون خروجی؛ کد خروج را با `echo $?` بررسی کنید):

`selinuxenabled`

- بررسی فعال بودن SELinux و چاپ نتیجه:

`selinuxenabled && echo "SELinux is enabled" || echo "SELinux is disabled"`

- استفاده در اسکریپت پوسته برای اجرای شرطی دستورها:

`if selinuxenabled; then echo "SELinux is running"; fi`
