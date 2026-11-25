# virt-xml-validate

> اعتبارسنجی فایل‌های XML مربوط به `libvirt` در برابر schema.
> اگر schema مشخص نشود، از عنصر ریشهٔ فایل XML تعیین می‌شود.
> اطلاعات بیشتر: <https://libvirt.org/manpages/virt-xml-validate.html>.

- اعتبارسنجی فایل XML در برابر schema مشخص:

`virt-xml-validate {{path/to/file.xml}} {{schema}}`

- اعتبارسنجی XML دامنه در برابر schema دامنه:

`virt-xml-validate {{path/to/domain.xml}} domain`
