# qm start

> شروع ماشین مجازی در مدیر ماشین مجازی QEMU/KVM.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_start>.

- شروع ماشین مجازی مشخص:

`qm start {{100}}`

- تعیین نوع ماشین QEMU (یعنی CPU قابل شبیه‌سازی):

`qm start {{100}} --machine {{q35}}`

- شروع ماشین مجازی مشخص با مهلت ۶۰ ثانیه:

`qm start {{100}} --timeout 60`
