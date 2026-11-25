# aurvote

> رأی دادن به بسته‌های مخزن کاربران آرچ.
> برای امکان رأی دادن، فایل `~/.config/aurvote` باید وجود داشته باشد و حاوی اعتبارنامه‌های AUR شما باشد.
> اطلاعات بیشتر: <https://github.com/archlinuxfr/aurvote#name>.

- ایجاد تعاملی فایل `~/.config/aurvote` حاوی نام کاربری و رمز عبور AUR شما:

`aurvote --configure`

- رأی دادن به یک یا چند بستهٔ AUR:

`aurvote {{package1 package2 ...}}`

- پس گرفتن رأی از یک یا چند بستهٔ AUR:

`aurvote {{[-u|--unvote]}} {{package1 package2 ...}}`

- بررسی اینکه آیا قبلاً به یک یا چند بستهٔ AUR رأی داده شده است:

`aurvote {{[-c|--check]}} {{package1 package2 ...}}`

- نمایش راهنما:

`aurvote {{[-h|--help]}}`
