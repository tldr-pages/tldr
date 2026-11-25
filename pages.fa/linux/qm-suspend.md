# qm suspend

> تعلیق ماشین مجازی در محیط مجازی Proxmox (PVE).
> از گزینه‌های `--skiplock` و `--skiplockstorage` با احتیاط استفاده کنید، زیرا در برخی شرایط ممکن است موجب خرابی داده شوند.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_suspend>.

- تعلیق ماشین مجازی با شناسه:

`qm {{[su|suspend]}} {{100}} {{integer}}`

- صرف‌نظر از بررسی قفل هنگام تعلیق ماشین مجازی:

`qm {{[su|suspend]}} {{100}} {{integer}} --skiplock`

- صرف‌نظر از بررسی قفل فضای ذخیره‌سازی هنگام تعلیق ماشین مجازی:

`qm {{[su|suspend]}} {{100}} {{integer}} --skiplockstorage`
