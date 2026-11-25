# lxc network

> مدیریت شبکه‌های کانتینرهای LXD.
> اطلاعات بیشتر: <https://canonical.com/lxd/docs/latest/reference/manpages/lxc/network/>.

- فهرست کردن همهٔ شبکه‌های موجود:

`lxc network list`

- نمایش پیکربندی شبکهٔ مشخص:

`lxc network show {{network_name}}`

- افزودن نمونهٔ در حال اجرا به شبکهٔ مشخص:

`lxc network attach {{network_name}} {{container_name}}`

- ایجاد شبکهٔ مدیریت‌شدهٔ جدید:

`lxc network create {{network_name}}`

- تنظیم واسط پل برای شبکهٔ مشخص:

`lxc network set {{network_name}} bridge.external_interfaces {{eth0}}`

- غیرفعال کردن NAT برای شبکهٔ مشخص:

`lxc network set {{network_name}} ipv{{4}}.nat false`
