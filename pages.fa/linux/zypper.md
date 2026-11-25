# zypper

> ابزار مدیریت بستهٔ SUSE و openSUSE.
> برای دستورهای معادل در سایر مدیران بسته، <https://wiki.archlinux.org/title/Pacman/Rosetta> را ببینید.
> اطلاعات بیشتر: <https://en.opensuse.org/SDB:Zypper_manual>.

- همگام‌سازی فهرست بسته‌ها و نسخه‌های موجود:

`sudo zypper {{[ref|refresh]}}`

- نصب بستهٔ جدید:

`sudo zypper {{[in|install]}} {{package}}`

- حذف بسته:

`sudo zypper {{[rm|remove]}} {{package}}`

- ارتقای بسته‌های نصب‌شده به جدیدترین نسخه‌های موجود:

`sudo zypper {{[up|update]}}`

- جست‌وجوی بسته با کلیدواژه:

`zypper {{[se|search]}} {{keyword}}`

- نمایش اطلاعات مربوط به مخازن پیکربندی‌شده:

`zypper {{[lr|repos]}} --sort-by-priority`
