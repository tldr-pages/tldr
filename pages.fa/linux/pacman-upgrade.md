# pacman --upgrade

> نصب دستی بسته‌ها از فایل‌های بایگانی.
> اطلاعات بیشتر: <https://manned.org/pacman.8>.

- نصب یک یا چند بسته از فایل‌ها:

`sudo pacman -U {{path/to/package1.pkg.tar.zst path/to/package2.pkg.tar.zst ...}}`

- نصب بسته بدون پرسش تأیید:

`sudo pacman -U --noconfirm {{path/to/package.pkg.tar.zst}}`

- بازنویسی فایل‌های متعارض هنگام نصب بسته:

`sudo pacman -U --overwrite {{path/to/file}} {{path/to/package.pkg.tar.zst}}`

- نصب بسته بدون بررسی نسخهٔ وابستگی‌ها:

`sudo pacman -Ud {{path/to/package.pkg.tar.zst}}`

- دریافت و چاپ بسته‌هایی که از ارتقا تأثیر می‌گیرند (هیچ بسته‌ای نصب نمی‌شود):

`pacman -Up {{path/to/package.pkg.tar.zst}}`

- نمایش راهنما:

`pacman -Uh`
