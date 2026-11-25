# audit2why

> توضیح موارد رد دسترسی SELinux بر اساس گزارش‌های ممیزی.
> بخشی از بستهٔ `policycoreutils-python-utils` است.
> همچنین : `audit2allow`, `ausearch`, `sealert`.
> اطلاعات بیشتر: <https://manned.org/audit2why>.

- توضیح جدیدترین مورد رد دسترسی SELinux:

`sudo audit2why`

- توضیح موارد رد دسترسی SELinux از یک فایل گزارش ممیزی مشخص:

`sudo audit2why {{[-i|--input]}} {{path/to/audit.log}}`

- توضیح همهٔ موارد رد دسترسی SELinux از گزارش ممیزی:

`sudo ausearch {{[-m|--message]}} avc | audit2why`

- توضیح موارد رد دسترسی برای یک سرویس مشخص:

`sudo ausearch {{[-m|--message]}} avc {{[-c|--comm]}} {{service_name}} | audit2why`
