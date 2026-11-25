# dnf4

> مدیر بسته برای RHEL 8/9 و نسخه‌های قدیمی فدورا (پیش از 41).
> برای دستورهای معادل در دیگر مدیران بسته، <https://wiki.archlinux.org/title/Pacman/Rosetta> را ببینید.
> اطلاعات بیشتر: <https://dnf.readthedocs.io/en/latest/command_ref.html>.

- ارتقای بسته‌های نصب‌شده به آخرین نسخه‌های موجود:

`sudo dnf4 {{[up|upgrade]}}`

- جست‌وجوی بسته‌ها با کلیدواژه‌ها:

`dnf4 {{[se|search]}} {{keyword1 keyword2 ...}}`

- نمایش جزئیات یک بسته:

`dnf4 {{[if|info]}} {{package}}`

- نصب یک بستهٔ جدید (برای تأیید خودکار همهٔ درخواست‌ها از `--assumeyes` استفاده کنید):

`sudo dnf4 {{[in|install]}} {{package1 package2 ...}}`

- حذف یک بسته:

`sudo dnf4 {{[rm|remove]}} {{package1 package2 ...}}`

- فهرست کردن بسته‌های نصب‌شده:

`dnf4 {{[ls|list]}} --installed`

- یافتن بسته‌هایی که یک دستور مشخص را ارائه می‌دهند:

`dnf4 {{[wp|provides]}} {{command}}`

- مشاهدهٔ همهٔ عملیات گذشته:

`dnf4 {{[hist|history]}}`
