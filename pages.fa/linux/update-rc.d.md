# update-rc.d

> نصب و حذف سرویس‌هایی که پیوندهای اسکریپت init به سبک System-V هستند.
> اسکریپت‌های init در `/etc/init.d/` قرار دارند.
> اطلاعات بیشتر: <https://manned.org/update-rc.d>.

- نصب سرویس:

`update-rc.d {{mysql}} defaults`

- فعال کردن سرویس:

`update-rc.d {{mysql}} enable`

- غیرفعال کردن سرویس:

`update-rc.d {{mysql}} disable`

- حذف اجباری سرویس:

`update-rc.d -f {{mysql}} remove`
