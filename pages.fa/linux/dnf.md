# dnf

> ابزار مدیریت بسته‌ها برای RHEL، Fedora و CentOS (جایگزین `yum`).
> برای دستورات معادل در دیگر مدیران بسته، به <https://wiki.archlinux.org/title/Pacman/Rosetta> مراجعه کنید.
> اطلاعات بیشتر: <https://dnf.readthedocs.io>.

- ارتقاء بسته‌های نصب شده به جدیدترین نسخه‌های موجود:

`sudo dnf upgrade`

- جستجوی بسته‌ها بر اساس کلمات کلیدی:

`dnf search {{keyword1 keyword2 ...}}`

- نمایش جزئیات یک بسته:

`dnf info {{package}}`

- نصب یک بسته جدید (از `-y` برای تأیید اتوماتیک تمام پنجره‌ها استفاده کنید):

`sudo dnf install {{package1 package2 ...}}`

- حذف یک بسته:

`sudo dnf remove {{package1 package2 ...}}`

- لیست بسته‌های نصب شده:

`dnf list --installed`

- یافتن بسته‌هایی که دستور مشخصی را ارائه می‌دهند:

`dnf provides {{command}}`

- مشاهده تاریخچه تمام عملیات‌های گذشته:

`dnf history`
