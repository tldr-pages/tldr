# virt-sparsify

> کم‌حجم کردن تصاویر دیسک ماشین مجازی با تخصیص پویا.
> توجه: برای جلوگیری از خرابی داده فقط برای ماشین‌های خاموش استفاده کنید.
> اطلاعات بیشتر: <https://manned.org/virt-sparsify>.

- ایجاد تصویر فشرده و کم‌حجم بدون snapshot از تصویر کم‌حجم‌نشده:

`virt-sparsify --compress {{path/to/image.qcow2}} {{path/to/new_image.qcow2}}`

- کم‌حجم کردن تصویر در همان محل:

`virt-sparsify --in-place {{path/to/image.img}}`

- تبدیل تصویر از یک قالب به قالب دیگر:

`virt-sparsify {{path/to/image}} --convert {{qcow2|raw|vdi|...}} {{path/to/new_image}}`
