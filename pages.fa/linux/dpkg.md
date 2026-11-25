# dpkg

> مدیر بستهٔ دبیان.
> برای دستورهای معادل در دیگر مدیران بسته، <https://wiki.archlinux.org/title/Pacman/Rosetta> را ببینید.
> برخی زیردستورها مانند `deb` مستندات استفادهٔ جداگانه دارند.
> اطلاعات بیشتر: <https://manned.org/dpkg>.

- نصب یک بسته:

`sudo dpkg {{[-i|--install]}} {{path/to/file.deb}}`

- حذف یک بسته:

`sudo dpkg {{[-r|--remove]}} {{package}}`

- فهرست کردن بسته‌های نصب‌شده:

`dpkg {{[-l|--list]}} {{pattern}}`

- فهرست کردن محتویات یک بسته:

`dpkg {{[-L|--listfiles]}} {{package}}`

- فهرست کردن محتویات فایل بستهٔ محلی:

`dpkg {{[-c|--contents]}} {{path/to/file.deb}}`

- یافتن بسته‌ای که مالک یک فایل است:

`dpkg {{[-S|--search]}} {{path/to/file}}`

- حذف کامل یک بستهٔ نصب‌شده یا قبلاً حذف‌شده، همراه با پیکربندی آن:

`sudo dpkg {{[-P|--purge]}} {{package}}`
