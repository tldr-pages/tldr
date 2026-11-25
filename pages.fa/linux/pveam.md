# pveam

> مدیریت قالب‌های کانتینر LXC.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pveam.1.html>.

- به‌روزرسانی پایگاه دادهٔ قالب‌های کانتینر:

`pveam {{[u|update]}}`

- فهرست کردن قالب‌های موجود:

`pveam {{[a|available]}}`

- بارگیری قالب:

`pveam {{[d|download]}} {{local}} {{template_name}}`

- فهرست کردن قالب‌های بارگیری‌شده:

`pveam {{[l|list]}} {{local}}`

- فهرست کردن قالب‌های موجود در بخش مشخص:

`pveam {{[a|available]}} --section {{system|turnkeylinux|mail}}`

- حذف قالب:

`pveam {{[r|remove]}} {{local}}:{{vztmpl}}/{{template_name}}`
