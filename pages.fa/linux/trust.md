# trust

> عملیات روی مخزن سیاست اعتماد.
> اطلاعات بیشتر: <https://manned.org/trust>.

- فهرست کردن موارد مخزن سیاست اعتماد:

`trust list`

- فهرست کردن اطلاعات موارد مشخص در مخزن سیاست اعتماد:

`trust list --filter={{blocklist|ca-anchors|certificates|trust-policy}}`

- ذخیرهٔ لنگر اعتماد مشخص در مخزن سیاست اعتماد:

`trust anchor {{path/to/certificate.crt}}`

- حذف لنگر مشخص از مخزن سیاست اعتماد:

`trust anchor --remove {{path/to/certificate.crt}}`

- استخراج سیاست اعتماد از مخزن اشتراکی سیاست اعتماد:

`trust extract --format=x509-directory --filter=ca-anchors {{path/to/directory}}`

- نمایش راهنمای زیردستور:

`trust {{subcommand}} --help`
