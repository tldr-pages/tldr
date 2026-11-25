# pvenode config

> دریافت و تنظیم پیکربندی گره.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pvenode.1.html#cli_pvenode_config_get>.

- نمایش کل پیکربندی موجود در `/etc/pve/nodes/node_name/config`:

`pvenode {{[co|config]}} {{[g|get]}}`

- نمایش ویژگی مشخص:

`pvenode {{[co|config]}} {{[g|get]}} --property {{property_name}}`

- تنظیم توضیح گره نمایش‌داده‌شده در زبانهٔ «Notes»:

`pvenode {{[co|config]}} {{[s|set]}} --description {{description_text}}`

- تنظیم اطلاعات مکان گره:

`pvenode {{[co|config]}} {{[s|set]}} --location latitude={{latitude}},longitude={{longitude}}`

- حذف تنظیم:

`pvenode {{[co|config]}} {{[s|set]}} --delete {{property_name}}`
