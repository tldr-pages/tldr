# cephadm

> استقرار و مدیریت یک خوشهٔ Ceph با استفاده از کانتینرها.
> بخشی از چارچوب هماهنگ‌سازی Ceph است.
> اطلاعات بیشتر: <https://docs.ceph.com/en/latest/man/8/cephadm/>.

- راه‌اندازی اولیهٔ یک خوشهٔ جدید Ceph روی میزبان فعلی:

`sudo cephadm bootstrap --mon-ip {{monitor_ip}}`

- افزودن یک میزبان جدید به خوشه:

`sudo cephadm add-host {{hostname}} {{ip_address}}`

- استقرار یک سرویس مشخص (مانند mgr، mon یا osd):

`sudo cephadm deploy {{service_type}} --name {{service_name}}`

- بررسی وضعیت سرویس‌های خوشه:

`sudo cephadm shell -- ceph {{[-s|--status]}}`

- ورود به محیط پوسته درون کانتینر Ceph:

`sudo cephadm shell`

- حذف یک سرویس از خوشه:

`sudo cephadm rm-service {{service_type}} --name {{service_name}}`
