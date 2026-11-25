# dnf versionlock

> محافظت از بسته‌ها در برابر به‌روزرسانی به نسخه‌های جدیدتر.
> به‌صورت پیش‌فرض بخشی از `dnf` نیست، اما از طریق `dnf-plugins-core` پشتیبانی می‌شود.
> اطلاعات بیشتر: <https://dnf-plugins-core.readthedocs.io/en/latest/versionlock.html>.

- فهرست کردن موارد فعلی قفل نسخه:

`dnf versionlock`

- افزودن قفل نسخه برای همهٔ بسته‌های موجود مطابق با مشخصات:

`dnf versionlock add {{package}}`

- افزودن استثنا در قفل نسخه برای بسته‌های موجود مطابق با مشخصات:

`dnf versionlock exclude {{package}}`

- حذف موارد قفل نسخهٔ مطابق:

`dnf versionlock delete {{package}}`

- حذف همهٔ موارد قفل نسخه:

`dnf versionlock clear`
