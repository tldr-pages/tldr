# dnf5 copr

> مدیریت مخازن Copr در سیستم‌های مبتنی بر فدورا.
> اطلاعات بیشتر: <https://dnf5.readthedocs.io/en/latest/dnf5_plugins/copr.8.html>.

- فعال کردن یک مخزن Copr:

`sudo dnf5 copr enable {{owner}}/{{project}}`

- فعال کردن یک مخزن Copr برای chroot مشخص:

`sudo dnf5 copr enable {{owner}}/{{project}} {{fedora-rawhide-ppc64le}}`

- فعال کردن یک مخزن Copr از یک هاب مشخص:

`sudo dnf5 copr enable {{hub}}/{{owner}}/{{project}}`

- غیرفعال کردن یک مخزن Copr:

`sudo dnf5 copr disable {{owner}}/{{project}}`

- حذف یک مخزن Copr:

`sudo dnf5 copr remove {{owner}}/{{project}}`

- فهرست کردن مخازن Copr:

`dnf5 copr list`

- چاپ اطلاعات اشکال‌زدایی سیستم:

`dnf5 copr debug`
