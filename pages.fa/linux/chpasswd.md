# chpasswd

> تغییر رمز عبور چند کاربر با استفاده از ورودی استاندارد `stdin`.
> همچنین : `passwd`.
> اطلاعات بیشتر: <https://manned.org/chpasswd>.

- تغییر رمز عبور یک کاربر مشخص:

`printf "{{username}}:{{new_password}}" | sudo chpasswd`

- تغییر رمز عبور چند کاربر (متن ورودی نباید حاوی فاصله باشد):

`printf "{{username_1}}:{{new_password_1}}\n{{username_2}}:{{new_password_2}}" | sudo chpasswd`

- تغییر رمز عبور یک کاربر مشخص با ارائهٔ آن به‌شکل رمزگذاری‌شده:

`printf "{{username}}:{{new_encrypted_password}}" | sudo chpasswd {{[-e|--encrypted]}}`

- تغییر رمز عبور یک کاربر مشخص با استفاده از روش رمزگذاری مشخص برای رمز ذخیره‌شده:

`printf "{{username}}:{{new_password}}" | sudo chpasswd {{[-c|--crypt-method]}} {{NONE|DES|MD5|SHA256|SHA512}}`
