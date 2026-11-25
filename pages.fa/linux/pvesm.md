# pvesm

> مدیریت فضای ذخیره‌سازی Proxmox.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pvesm.1.html>.

- دریافت وضعیت همهٔ مخازن داده:

`pvesm {{[st|status]}}`

- فهرست کردن محتویات فضای ذخیره‌سازی:

`pvesm {{[l|list]}} {{storage_name}}`

- مشاهدهٔ مسیر فایل ذخیره‌شده:

`pvesm {{[pa|path]}} {{storage_name}}:{{content_type}}/{{file_name}}`

- افزودن فضای ذخیره‌سازی دایرکتوری:

`pvesm {{[ad|add]}} dir {{storage_name}} --path {{path/to/directory}}`

- تنظیم فضای ذخیره‌سازی برای داشتن محتوای مشخص:

`pvesm {{[se|set]}} {{storage_name}} --content {{iso,images,backup,vztmpl,rootdir,snippets,import}}`

- حذف فایل از فضای ذخیره‌سازی:

`pvesm {{[f|free]}} {{local:iso/archlinux-2025.08.01-x86_64.iso}}`

- حذف فضای ذخیره‌سازی:

`pvesm {{[r|remove]}} {{storage_name}}`
