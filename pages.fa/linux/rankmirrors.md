# rankmirrors

> رتبه‌بندی فهرست آینه‌های Pacman بر اساس سرعت اتصال و باز شدن.
> فهرست جدید آینه‌ها را در `stdout` می‌نویسد.
> اطلاعات بیشتر: <https://manned.org/rankmirrors>.

- رتبه‌بندی فهرست آینه‌ها:

`rankmirrors {{/etc/pacman.d/mirrorlist}}`

- خروجی فقط تعداد مشخصی از سرورهای برتر:

`rankmirrors -n {{number}} {{/etc/pacman.d/mirrorlist}}`

- نمایش خروجی مفصل هنگام تولید فهرست آینه‌ها:

`rankmirrors {{[-v|--verbose]}} {{/etc/pacman.d/mirrorlist}}`

- آزمایش فقط URL مشخص:

`rankmirrors {{[-u|--url]}} {{url}}`

- خروجی فقط زمان پاسخ به‌جای فهرست کامل آینه‌ها:

`rankmirrors {{[-t|--times]}} {{/etc/pacman.d/mirrorlist}}`
