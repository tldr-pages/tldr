# rpcinfo

> فراخوانی RPC در سرور RPC و گزارش نتیجه.
> اطلاعات بیشتر: <https://manned.org/rpcinfo>.

- نمایش جدول کامل همهٔ سرویس‌های RPC ثبت‌شده در localhost:

`rpcinfo`

- نمایش جدول مختصر همهٔ سرویس‌های RPC ثبت‌شده در localhost:

`rpcinfo -s localhost`

- نمایش جدول آمار عملیات rpcbind در localhost:

`rpcinfo -m`

- نمایش فهرست مدخل‌های نام سرویس مشخص (mountd) و شمارهٔ نسخه (۲) در اشتراک nfs راه دور:

`rpcinfo -l {{remote_nfs_server_ip}} mountd 2`

- حذف ثبت نسخهٔ ۱ سرویس mountd برای همهٔ روش‌های انتقال:

`rpcinfo -d mountd 1`
