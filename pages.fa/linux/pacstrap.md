# pacstrap

> نصب بسته‌های Arch Linux در دایرکتوری ریشهٔ جدید مشخص.
> اطلاعات بیشتر: <https://manned.org/pacstrap>.

- نصب بستهٔ `base`، هستهٔ لینوکس و میان‌افزار سخت‌افزارهای رایج:

`pacstrap {{path/to/new_root}} {{base}} {{linux}} {{linux-firmware}}`

- نصب بستهٔ `base`، هستهٔ LTS لینوکس و ابزارهای ساخت `base-devel`:

`pacstrap {{path/to/new_root}} {{base}} {{base-devel}} {{linux-lts}}`

- نصب بسته‌ها و کپی پیکربندی Pacman میزبان در مقصد:

`pacstrap -P {{path/to/new_root}} {{packages}}`

- نصب بسته‌ها بدون کپی فهرست آینهٔ میزبان در مقصد:

`pacstrap -M {{path/to/new_root}} {{packages}}`

- استفاده از فایل پیکربندی جایگزین برای Pacman:

`pacstrap -C {{path/to/pacman.conf}} {{path/to/new_root}} {{packages}}`

- نصب بسته‌ها با استفاده از حافظهٔ نهان بسته‌های میزبان به‌جای مقصد:

`pacstrap -c {{path/to/new_root}} {{packages}}`

- مقداردهی اولیهٔ حلقهٔ کلید خالی `pacman` در مقصد بدون کپی آن از میزبان:

`pacstrap -K {{path/to/new_root}} {{packages}}`

- نصب بسته‌ها در حالت تعاملی (درخواست تأیید):

`pacstrap -i {{path/to/new_root}} {{packages}}`
