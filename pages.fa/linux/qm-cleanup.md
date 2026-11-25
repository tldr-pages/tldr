# qm cleanup

> پاک‌سازی منابع در مدیر ماشین مجازی QEMU/KVM مانند دستگاه‌های tap و VGPUها.
> پس از خاموش شدن، خرابی و غیرهٔ ماشین مجازی فراخوانی می‌شود.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_cleanup>.

- پاک‌سازی منابع:

`qm {{[cle|cleanup]}} {{100}} {{true|false}} {{true|false}}`

- اطلاع به سیستم که ماشین مجازی به‌درستی خاموش نشده است:

`qm {{[cle|cleanup]}} {{100}} false {{true|false}}`

- اطلاع به سیستم که خاموشی توسط مهمان درخواست شده است:

`qm {{[cle|cleanup]}} {{100}} {{true|false}} true`
