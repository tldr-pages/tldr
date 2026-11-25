# virt-manager

> رابط کاربری دسکتاپ برای مدیریت ماشین‌های مجازی KVM و Xen و کانتینرهای LXC.
> اطلاعات بیشتر: <https://manned.org/virt-manager>.

- اجرای رابط گرافیکی:

`virt-manager`

- اتصال به hypervisor:

`virt-manager --connect {{hypervisor_uri}}`

- اجرا نکردن فرایند virt-manager در پس‌زمینه هنگام شروع:

`virt-manager --no-fork`

- چاپ خروجی اشکال‌زدایی:

`virt-manager --debug`

- باز کردن راهنمای ایجاد ماشین مجازی جدید:

`virt-manager --show-domain-creator`

- نمایش پنجرهٔ جزئیات دامنه برای ماشین مجازی یا کانتینر مشخص:

`virt-manager --show-domain-editor {{name|id|uuid}}`

- نمایش پنجرهٔ عملکرد دامنه برای ماشین مجازی یا کانتینر مشخص:

`virt-manager --show-domain-performance {{name|id|uuid}}`

- نمایش پنجرهٔ جزئیات اتصال:

`virt-manager --show-host-summary`
