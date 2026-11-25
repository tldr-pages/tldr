# rpmconf

> رسیدگی به فایل‌های `.rpmnew`، `.rpmsave` و `.rpmorig` باقی‌مانده پس از ارتقای بسته‌ها.
> همچنین : `rpm`.
> اطلاعات بیشتر: <https://manned.org/rpmconf.8>.

- فهرست کردن فایل‌های باقی‌مانده و انتخاب تعاملی اقدام برای هر یک:

`sudo rpmconf {{[-a|--all]}}`

- حذف فایل‌های یتیم `.rpmnew` و `.rpmsave`:

`sudo rpmconf {{[-a|--all]}} {{[-c|--clean]}}`
