# qm sendkey

> ارسال رویداد کلید با رمزگذاری QEMU monitor به ماشین مجازی.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_sendkey>.

- ارسال رویداد کلید مشخص به ماشین مجازی مشخص:

`qm {{[sen|sendkey]}} {{100}} {{key}}`

- اجازه به کاربر root برای ارسال رویداد کلید با نادیده گرفتن قفل‌ها:

`qm {{[sen|sendkey]}} --skiplock {{true}} {{100}} {{key}}`
