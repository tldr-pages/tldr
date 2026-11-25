# systemctl isolate

> شروع واحد مشخص همراه با وابستگی‌ها و توقف سایر واحدها.
> واحدهای دارای `IgnoreOnIsolate=yes` را نادیده می‌گیرد.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#isolate%20UNIT>.

- تغییر به هدف (در صورت نبود پسوند `.target` فرض می‌شود):

`systemctl isolate {{target}}`

- تغییر صریح به هدف گرافیکی:

`systemctl isolate graphical.target`

- تغییر به حالت نجات (تک‌کاربره):

`systemctl isolate rescue.target`

- تغییر به حالت اضطراری:

`systemctl isolate emergency.target`
