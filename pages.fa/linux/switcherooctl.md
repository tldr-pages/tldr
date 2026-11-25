# switcherooctl

> اجرای دستور روی GPU مشخص.
> اطلاعات بیشتر: <https://manned.org/switcherooctl>.

- فعال کردن سرویس switcheroo:

`systemctl start switcheroo-control`

- فهرست کردن GPUهای شناخته‌شده:

`switcherooctl`

- اجرای دستور روی نخستین GPU مجزا:

`switcherooctl launch {{command}}`

- اجرای دستور روی GPU مشخص:

`switcherooctl launch {{[-g|--gpu]}} {{device_number}} {{command}}`

- نمایش راهنما:

`switcherooctl help`
