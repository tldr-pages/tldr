# systemctl mount-image

> سوار کردن فایل تصویر در فضای نام اتصال واحد.
> فقط برای واحدهایی پشتیبانی می‌شود که در فضای اتصال اجرا می‌شوند، مانند واحدهای دارای `RootImage=` یا `PrivateMounts=`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#mount-image%20UNIT%20IMAGE%20%5BPATH%20%5BPARTITION_NAME:MOUNT_OPTIONS%5D%5D>.

- سوار کردن تصویر در مسیر مشخص داخل فضای نام اتصال واحد:

`systemctl mount-image {{unit}} /{{path/to/image}} /{{path/to/directory_inside_unit}}`

- سوار کردن پارتیشن `root` تصویر با گزینه‌های فقط‌خواندنی و no-setuid:

`systemctl mount-image {{unit}} /{{path/to/image}} /{{path/to/directory_inside_unit}} root:ro,nosuid`

- ایجاد دایرکتوری مقصد پیش از اتصال:

`systemctl mount-image --mkdir {{unit}} /{{path/to/image}} /{{path/to/directory_inside_unit}}`

- سوار کردن تصویر به‌صورت فقط‌خواندنی:

`systemctl mount-image --read-only {{unit}} /{{path/to/image}} /{{path/to/directory_inside_unit}}`
