# qm guest

> مدیریت عامل مهمان ماشین مجازی.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_guest_cmd>.

- چاپ وضعیت PID مشخص:

`qm {{[g|guest]}} {{[exec-s|exec-status]}} {{100}} {{process_id}}`

- تنظیم تعاملی رمز عبور کاربر مشخص در ماشین مجازی:

`qm {{[g|guest]}} {{[p|passwd]}} {{100}} {{username}}`

- تنظیم تعاملی رمز عبور ازپیش‌هش‌شده برای کاربر مشخص در ماشین مجازی:

`qm {{[g|guest]}} {{[p|passwd]}} {{100}} {{username}} --crypted 1`

- اجرای دستور مشخص عامل مهمان QEMU:

`qm {{[g|guest]}} {{[c|cmd]}} {{100}} {{fsfreeze-freeze|fsfreeze-status|fsfreeze-thaw|fstrim|get-fsinfo|...}}`

- اجرای دستور مشخص از طریق عامل مهمان:

`qm {{[g|guest]}} exec {{100}} {{command}} {{argument1 argument2 ...}}`

- اجرای ناهمگام دستور مشخص از طریق عامل مهمان:

`qm {{[g|guest]}} exec {{100}} {{argument1 argument2 ...}} --synchronous 0`

- اجرای دستور مشخص از طریق عامل مهمان با مهلت ۱۰ ثانیه:

`qm {{[g|guest]}} exec {{100}} {{argument1 argument2...}} --timeout {{10}}`

- اجرای دستور مشخص از طریق عامل مهمان و ارسال ورودی `stdin` تا EOF به عامل مهمان:

`qm {{[g|guest]}} exec {{100}} {{argument1 argument2 ...}} --pass-stdin 1`
