# dnf config-manager

> مدیریت گزینه‌های پیکربندی و مخازن DNF در سیستم‌های مبتنی بر فدورا.
> به‌صورت پیش‌فرض بخشی از `dnf` نیست، اما از طریق `dnf-plugins-core` پشتیبانی می‌شود.
> اطلاعات بیشتر: <https://dnf-plugins-core.readthedocs.io/en/latest/config_manager.html>.

- افزودن و فعال کردن یک مخزن از URL:

`dnf config-manager --add-repo={{repository_url}}`

- چاپ مقادیر پیکربندی فعلی:

`dnf config-manager --dump`

- فعال کردن یک مخزن مشخص:

`dnf config-manager {{[--enable|--set-enabled]}} {{repository_id}}`

- غیرفعال کردن مخازن مشخص:

`dnf config-manager {{[--disable|--set-disabled]}} {{repository_id1 repository_id2 ...}}`

- تنظیم یک گزینهٔ پیکربندی برای مخزن:

`dnf config-manager --setopt={{option}}={{value}}`

- نمایش راهنما:

`dnf config-manager --help-cmd`
