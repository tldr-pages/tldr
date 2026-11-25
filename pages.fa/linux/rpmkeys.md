# rpmkeys

> ابزار وارد و حذف کردن کلیدهای RPM برای مخازن RPM.
> هنگام افزودن مخزن RPM باید کلید RPM متناظر را نیز وارد کنید.
> اطلاعات بیشتر: <https://rpm-software-management.github.io/rpm/man/rpmkeys.8>.

- فهرست کردن همهٔ کلیدهای RPM واردشده؛ شناسهٔ کلید لازم برای حذف را نیز نمایش می‌دهد:

`sudo rpmkeys --list`

- حذف کلید RPM قبلاً واردشده با شناسهٔ ۱۶ رقمی یا حرفی آن:

`sudo rpmkeys --delete {{5a278d9c-5bbc73cb}}`

- وارد کردن کلید RPM مخزن:

`sudo rpmkeys --import {{path/to/rpm_key}}`
