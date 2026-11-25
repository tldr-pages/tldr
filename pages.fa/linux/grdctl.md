# grdctl

> مدیریت سرویس میزکار راه دور GNOME.
> اطلاعات بیشتر: <https://github.com/GNOME/gnome-remote-desktop/blob/main/man/grdctl.txt>.

- فهرست کردن تنظیمات فعلی GRD:

`grdctl status`

- فعال کردن سرویس‌های پشتیبان پروتکل میزکار راه دور (RDP) یا رایانش شبکهٔ مجازی (VNC):

`grdctl {{rdp|vnc}} enable`

- تنظیم اعتبارنامه‌های RDP:

`grdctl rdp set-credentials {{username}} {{password}}`

- تنظیم رمز عبور VNC:

`grdctl vnc set-password {{password}}`

- فعال کردن کنترل راه دور دستگاه‌های ورودی:

`grdctl {{rdp|vnc}} disable-view-only`

- غیرفعال کردن کنترل راه دور دستگاه‌های ورودی:

`grdctl {{rdp|vnc}} enable-view-only`

- غیرفعال کردن سرویس‌های پشتیبان RDP یا VNC:

`grdctl {{rdp|vnc}} disable`
