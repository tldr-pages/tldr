# qm remote-migrate

> مهاجرت ماشین مجازی به میزبان یا خوشهٔ راه دور Proxmox.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_remote-migrate>.

- مهاجرت ماشین مجازی به میزبان راه دور:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}}' --target-bridge {{bridge}} --target-storage {{storage}}`

- مهاجرت زندهٔ ماشین مجازی در حال اجرا:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}}' --target-bridge {{bridge}} --target-storage {{storage}} --online`

- حذف ماشین مجازی مبدأ پس از مهاجرت موفق:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}}' --target-bridge {{bridge}} --target-storage {{storage}} --delete 1`

- محدود کردن پهنای باند مهاجرت:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}}' --target-bridge {{bridge}} --target-storage {{storage}} --bwlimit {{value}}`

- استفاده از همان نام‌های پل و فضای ذخیره‌سازی در مقصد:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}}' --target-bridge 1 --target-storage 1`

- اتصال به API راه دور روی پورت دلخواه:

`qm remote-migrate {{vmid}} {{target_vmid}} 'apitoken=PVEAPIToken={{user}}@{{realm}}!{{token}}={{secret}},host={{address}},fingerprint={{fingerprint}},port={{porta}}' --target-bridge {{bridge}} --target-storage {{storage}}`
