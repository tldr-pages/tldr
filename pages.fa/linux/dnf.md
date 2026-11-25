# dnf

> مدیر بسته برای Fedora 41 و جدیدتر و RHEL 10.
> برای دستورهای معادل در دیگر مدیران بسته، <https://wiki.archlinux.org/title/Pacman/Rosetta> را ببینید.
> اطلاعات بیشتر: <https://dnf5.readthedocs.io/en/latest/commands/index.html>.

- ارتقای بسته‌های نصب‌شده به آخرین نسخه‌های موجود:

`sudo dnf {{[up|upgrade]}}`

- جست‌وجوی بسته‌ها با کلیدواژه‌ها:

`dnf {{[se|search]}} {{keyword1 keyword2 ...}}`

- نمایش جزئیات یک بسته:

`dnf {{[if|info]}} {{package}}`

- نصب بسته‌های جدید (برای تأیید خودکار همهٔ درخواست‌ها از `--assumeyes` استفاده کنید):

`sudo dnf {{[in|install]}} {{package1 package2 ...}}`

- حذف بسته‌ها:

`sudo dnf {{[rm|remove]}} {{package1 package2 ...}}`

- فهرست کردن بسته‌های نصب‌شده:

`dnf {{[ls|list]}} --installed`

- یافتن بسته‌هایی که یک دستور مشخص را ارائه می‌دهند:

`dnf provides {{command}}`

- پاکسازی داده‌های حافظهٔ نهان:

`sudo dnf clean {{all|dbcache|expire-cache|metadata|packages}}`
