# nova

> پروژهٔ OpenStack که روشی برای فراهم‌سازی نمونه‌های محاسباتی ارائه می‌دهد.
> اطلاعات بیشتر: <https://docs.openstack.org/nova/latest/>.

- فهرست کردن ماشین‌های مجازی مستأجر فعلی:

`nova list`

- فهرست کردن ماشین‌های مجازی همهٔ مستأجران (فقط کاربر مدیر):

`nova list --all-tenants`

- راه‌اندازی ماشین مجازی روی میزبان مشخص:

`nova boot --nic net-id={{net_id}} --image {{image_id}} --flavor {{flavor}} --availability-zone nova:{{host_name}} {{vm_name}}`

- شروع سرور:

`nova start {{server}}`

- توقف سرور:

`nova stop {{server}}`

- اتصال واسط شبکه به ماشین مجازی مشخص:

`nova interface-attach --net-id {{net_id}} {{server}}`
