# ceph

> یک سامانهٔ ذخیره‌سازی یکپارچه.
> اطلاعات بیشتر: <https://docs.ceph.com/en/latest/man/8/ceph/>.

- بررسی وضعیت سلامت خوشه:

`ceph status`

- بررسی آمار استفاده از خوشه:

`ceph df`

- دریافت آمار گروه‌های جای‌گذاری در یک خوشه:

`ceph pg dump --format {{plain}}`

- ایجاد یک مخزن ذخیره‌سازی:

`ceph osd pool create {{pool_name}} {{page_number}}`

- حذف یک مخزن ذخیره‌سازی:

`ceph osd pool delete {{pool_name}}`

- تغییر نام یک مخزن ذخیره‌سازی:

`ceph osd pool rename {{current_name}} {{new_name}}`

- تعمیر خودکار فضای ذخیره‌سازی مخزن:

`ceph pg repair {{pool_name}}`
