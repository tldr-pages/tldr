# qm guest exec

> اجرای دستور مشخص از طریق عامل مهمان.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_guest_exec>.

- اجرای دستور مشخص از طریق عامل مهمان:

`qm {{[g|guest]}} exec {{100}} {{command}} {{argument1 argument2 ...}}`

- اجرای ناهمگام دستور مشخص از طریق عامل مهمان:

`qm {{[g|guest]}} exec {{100}} {{argument1 argument2 ...}} --synchronous 0`

- اجرای دستور مشخص از طریق عامل مهمان با مهلت ۱۰ ثانیه:

`qm {{[g|guest]}} exec {{100}} {{argument1 argument2...}} --timeout {{10}}`

- اجرای دستور مشخص از طریق عامل مهمان و ارسال ورودی `stdin` تا EOF به عامل مهمان:

`qm {{[g|guest]}} exec {{100}} {{argument1 argument2 ...}} --pass-stdin 1`
