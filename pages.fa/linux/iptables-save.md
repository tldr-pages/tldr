# iptables-save

> ذخیرهٔ پیکربندی IPv4 دستور `iptables`.
> برای انجام همین کار در IPv6 از `ip6tables-save` استفاده کنید.
> اطلاعات بیشتر: <https://manned.org/iptables-save>.

- چاپ پیکربندی `iptables`:

`sudo iptables-save`

- چاپ پیکربندی جدول مشخص `iptables`:

`sudo iptables-save {{[-t|--table]}} {{table}}`

- ذخیرهٔ پیکربندی `iptables` در فایل:

`sudo iptables-save {{[-f|--file]}} {{path/to/file}}`
