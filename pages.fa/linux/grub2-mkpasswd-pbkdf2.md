# grub2-mkpasswd-pbkdf2

> تولید رمز عبور هش‌شده برای GRUB.
> اطلاعات بیشتر: <https://manned.org/grub2-mkpasswd-pbkdf2>.

- ایجاد هش رمز عبور GRUB 2 با PBKDF2 و چاپ آن در خروجی استاندارد `stdout`:

`sudo grub2-mkpasswd-pbkdf2 {{[-c|--iteration-count]}} {{number_of_pbkdf2_iterations}} {{[-s|--salt]}} {{salt_length}}`
