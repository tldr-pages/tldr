# pvecm

> مدیر خوشهٔ Proxmox VE.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pvecm.1.html>.

- افزودن گره فعلی به خوشهٔ موجود:

`pvecm add {{hostname_or_ip}}`

- افزودن گره به پیکربندی خوشه (استفادهٔ داخلی):

`pvecm {{[addn|addnode]}} {{node}}`

- نمایش نسخهٔ API پیوستن به خوشه که در این گره موجود است:

`pvecm {{[ap|apiver]}}`

- تولید پیکربندی جدید خوشه:

`pvecm {{[c|create]}} {{clustername}}`

- حذف گره از پیکربندی خوشه:

`pvecm {{[d|delnode]}} {{node}}`

- نمایش نمای محلی گره‌های خوشه:

`pvecm {{[n|nodes]}}`

- نمایش نمای محلی وضعیت خوشه:

`pvecm {{[s|status]}}`
