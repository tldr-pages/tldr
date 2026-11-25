# dnf clean

> پاکسازی فایل‌های موقت نگه‌داری‌شده برای مخازن مبتنی بر رد هت.
> اطلاعات بیشتر: <https://dnf.readthedocs.io/en/latest/command_ref.html#clean-command>.

- حذف فایل‌های حافظهٔ نهان تولیدشده از فرادادهٔ مخزن:

`dnf clean dbcache`

- علامت‌گذاری فرادادهٔ مخزن به‌عنوان منقضی‌شده:

`dnf clean expire-cache`

- حذف فرادادهٔ مخزن:

`dnf clean metadata`

- حذف بسته‌های ذخیره‌شده در حافظهٔ نهان سیستم:

`dnf clean packages`

- پاکسازی همهٔ فراداده و فایل‌های نهان مرتبط با مخازن DNF (همهٔ موارد بالا):

`dnf clean all`
