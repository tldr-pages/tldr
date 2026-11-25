# dnf changelog

> مشاهدهٔ گزارش‌های تغییرات یک بستهٔ مشخص.
> به‌صورت پیش‌فرض بخشی از `dnf` نیست، اما از طریق `dnf-plugins-core` پشتیبانی می‌شود.
> اطلاعات بیشتر: <https://dnf-plugins-core.readthedocs.io/en/latest/changelog.html>.

- مشاهدهٔ همهٔ گزارش‌های تغییرات یک بستهٔ مشخص:

`dnf changelog {{package}}`

- مشاهدهٔ همهٔ گزارش‌های تغییرات یک بستهٔ مشخص پس از تاریخ تعیین‌شده:

`dnf changelog --since {{date}} {{package}}`

- مشاهدهٔ تعداد مشخصی از آخرین گزارش‌های تغییرات یک بسته:

`dnf changelog --count {{number}} {{package}}`

- نمایش فقط موارد جدید برای بسته‌های قابل ارتقا:

`dnf changelog --upgrades {{package}}`

- نمایش راهنما:

`dnf changelog --help-cmd`
