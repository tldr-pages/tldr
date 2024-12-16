# grub2-mkpasswd-pbkdf2

> Set up a password to prevent unauthorized users from accessing the GRUB command line, modifying kernel command-line arguments, or booting non-default OSTree deployments.
> More information: <https://manned.org/grub2-mkpasswd-pbkdf2>.

- Create a password hash for GRUB 2 using PBKDF2 and print it to `stdout`:

`sudo grub2-mkpasswd-pbkdf2 {{-c|--iteration-count}} {{number_of_pbkdf2_iterations}} {{-s|--salt}} {{salt_length}}`
