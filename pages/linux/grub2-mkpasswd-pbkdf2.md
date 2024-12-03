# grub2-mkpasswd-pbkdf2

> You can set up a password to prevent unauthorized users from accessing the GRUB command line, modifying kernel command-line arguments, or booting non-default OSTree deployments.
> More information: <https://manned.org/grub2-mkpasswd-pbkdf2>.

- You can use grub2-mkpasswd-pbkdf2 to create a password hash for GRUB 2 using PBKDF2:

`sudo grub2-mkpasswd-pbkdf2 -c {{number}} -s {{mySaltValue}}`
