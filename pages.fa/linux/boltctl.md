# boltctl

> کنترل دستگاه‌های تاندربولت.
> اطلاعات بیشتر: <https://manned.org/boltctl>.

- فهرست کردن دستگاه‌های متصل و مجاز:

`boltctl`

- فهرست کردن دستگاه‌های متصل، از جمله دستگاه‌های غیرمجاز:

`boltctl list`

- مجاز کردن موقت یک دستگاه:

`boltctl authorize {{device_uuid}}`

- مجاز کردن و به خاطر سپردن یک دستگاه:

`boltctl enroll {{device_uuid}}`

- لغو مجوز یک دستگاه که قبلاً مجاز شده است:

`boltctl forget {{device_uuid}}`

- نمایش اطلاعات بیشتر دربارهٔ یک دستگاه:

`boltctl info {{device_uuid}}`
