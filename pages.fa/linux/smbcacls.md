# smbcacls

> مشاهده و تغییر ACLهای Windows روی اشتراک‌های SMB.
> بخشی از مجموعهٔ Samba.
> اطلاعات بیشتر: <https://www.samba.org/samba/docs/current/man-html/smbcacls.1.html>.

- نمایش ACLهای فایل یا دایرکتوری در اشتراک SMB راه دور:

`smbcacls //{{server}}/{{share}} {{path/to/file_or_directory}} --user {{domain\\username}}%{{password}}`

- تنظیم ACL جدید برای فایل در اشتراک SMB راه دور (به‌جای `"ACL:..."` مشخصات معتبر ACL ویندوز را قرار دهید):

`smbcacls //{{server}}/{{share}} {{path/to/file}} --user {{domain\\username}}%{{password}} "ACL:{{DACL}}"`

- حذف همهٔ مدخل‌های ACL موجود و تنظیم ACL جدید:

`smbcacls //{{server}}/{{share}} {{path/to/file}} --user {{domain\\username}}%{{password}} "RESET" "ACL:{{DACL}}"`

- تعیین گروه کاری یا دامنهٔ جایگزین و درخواست تعاملی رمز عبور:

`smbcacls //{{server}}/{{share}} {{path/to/file}} --user {{username}} --workgroup {{workgroup}}`
