# qm shutdown

> خاموش کردن ماشین مجازی در مدیر ماشین مجازی QEMU/KVM.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_shutdown>.

- خاموش کردن ماشین مجازی:

`qm {{[shu|shutdown]}} {{100}}`

- خاموش کردن ماشین مجازی پس از حداکثر ۱۰ ثانیه انتظار:

`qm {{[shu|shutdown]}} {{100}} --timeout 10`

- خاموش کردن ماشین مجازی بدون غیرفعال کردن حجم‌های ذخیره‌سازی:

`qm {{[shu|shutdown]}} {{100}} --keepActive true`

- خاموش کردن ماشین مجازی با صرف‌نظر از قفل (فقط root می‌تواند از این گزینه استفاده کند):

`qm {{[shu|shutdown]}} {{100}} --skiplock true`

- توقف و خاموش کردن ماشین مجازی:

`qm {{[shu|shutdown]}} {{100}} --forceStop true`
