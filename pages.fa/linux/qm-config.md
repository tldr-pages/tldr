# qm config

> نمایش پیکربندی ماشین مجازی با اعمال تغییرات پیکربندی در انتظار.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_config>.

- نمایش پیکربندی ماشین مجازی:

`qm {{[co|config]}} {{100}}`

- نمایش مقادیر پیکربندی فعلی به‌جای مقادیر در انتظار ماشین مجازی:

`qm {{[co|config]}} --current {{true}} {{100}}`

- دریافت مقادیر پیکربندی از snapshot مشخص:

`qm {{[co|config]}} --snapshot {{snapshot_name}} {{100}}`
