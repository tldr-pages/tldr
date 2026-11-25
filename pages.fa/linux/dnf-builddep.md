# dnf builddep

> نصب وابستگی‌های مورد نیاز برای ساخت یک بستهٔ مشخص.
> به‌صورت پیش‌فرض بخشی از `dnf` نیست، اما از طریق `dnf-plugins-core` پشتیبانی می‌شود.
> اطلاعات بیشتر: <https://dnf-plugins-core.readthedocs.io/en/latest/builddep.html>.

- نصب وابستگی‌های یک بستهٔ مشخص:

`dnf builddep {{path/to/specification.spec}}`

- نصب وابستگی‌های یک بستهٔ مشخص و نادیده گرفتن موارد ناموجود:

`dnf builddep --skip-unavailable {{path/to/specification.spec}}`

- تعریف ماکروی RPM با عبارت مشخص:

`dnf builddep {{[-D|--define]}} '{{expression}}'`

- تعریف آرگومانی برای مسیر فایل `.spec`:

`dnf builddep --spec {{argument}}`

- تعریف آرگومانی برای مسیر فایل `.rpm`:

`dnf builddep --srpm {{argument}}`

- نمایش راهنما:

`dnf builddep --help-cmd`
