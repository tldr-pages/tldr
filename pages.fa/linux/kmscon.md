# kmscon

> استفاده از framebuffer به‌جای حالت متنی برای رسم ترمینال در TTY.
> اطلاعات بیشتر: <https://manned.org/kmscon>.

- شروع `kmscon` در نخستین TTY موجود، مطابق گزارش `fgconsole --next-available`:

`sudo kmscon`

- شروع `kmscon` در TTY مشخص:

`sudo kmscon --vt {{/dev/ttyX|ttyX|X}}`

- فعال کردن پشتیبانی از ماوس:

`sudo kmscon --mouse`

- تعیین دستور مورد استفاده برای ورود:

`sudo kmscon {{[-l|--login]}} {{command}}`

- همیشه شروع کردن `kmscon` در ترمینال مشخص:

`systemctl enable --now kmsconvt@{{ttyX}}`
