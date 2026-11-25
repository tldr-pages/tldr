# pct exec

> اجرای دستور داخل کانتینر مشخص.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_exec>.

- اجرای دستور در کانتینر:

`pct {{[ex|exec]}} {{100}} {{command}}`

- باز کردن پوستهٔ Bash در کانتینر:

`pct {{[ex|exec]}} {{100}} bash`

- ارسال آرگومان‌ها به دستور:

`pct {{[ex|exec]}} {{100}} -- {{command}} {{arguments}}`
