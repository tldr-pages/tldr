# rpcclient

> ابزار کارخواه MS-RPC (بخشی از مجموعهٔ samba).
> اطلاعات بیشتر: <https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html>.

- اتصال به میزبان راه دور:

`rpcclient {{[-U|--user]}} {{domain}}\{{username}}%{{password}} {{ip_address}}`

- اتصال به میزبان راه دور در دامنه بدون رمز عبور:

`rpcclient {{[-U|--user]}} {{username}} {{[-W|--workgroup]}} {{domain}} {{[-N|--no-pass]}} {{ip_address}}`

- اتصال به میزبان راه دور با ارسال هش رمز عبور:

`rpcclient {{[-U|--user]}} {{domain}}\{{username}} --pw-nt-hash {{ip_address}}`

- اجرای دستورهای پوسته در میزبان راه دور:

`rpcclient {{[-U|--user]}} {{domain}}\{{username}}%{{password}} {{[-c|--command]}} {{semicolon_separated_commands}} {{ip_address}}`

- [تعاملی] نمایش کاربران دامنه:

`enumdomusers`

- [تعاملی] نمایش دسترسی‌ها:

`enumprivs`

- [تعاملی] نمایش اطلاعات کاربر مشخص:

`queryuser {{username|rid}}`

- [تعاملی] ایجاد کاربر جدید در دامنه:

`createdomuser {{username}}`
