# pveum

> مدیریت کاربران Proxmox.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pveum.1.html>.

- فهرست کردن کاربران:

`pveum {{[u|user]}} {{[l|list]}}`

- افزودن کاربر:

`pveum {{[u|user]}} {{[a|add]}} {{username}}@pve`

- افزودن کاربر با ایمیل، توضیح و رمز عبور:

`pveum {{[u|user]}} {{[a|add]}} {{username}}@pve --email {{email_address}} --comment {{description}} --password {{password}}`

- تغییر رمز عبور کاربر:

`pveum {{[pa|passwd]}} {{username}}@pve`

- حذف کاربر:

`pveum {{[u|user]}} {{[d|delete]}} {{username}}@pve`

- دادن دسترسی به ماشین مجازی مشخص با مجوزهای مشخص به کاربر:

`pveum {{[a|acl]}} {{[m|modify]}} /vms/{{1000}} --user {{username}}@pve --role {{PVEVMUser}}`
