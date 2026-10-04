# grub-fstest

> Debug tool for GRUB filesystem drivers.
> More information: <https://manpages.debian.org/testing/grub-common/grub-fstest.1.en.html>.

- List files in a filesystem image:

`grub-fstest {{path/to/filesystem.img}} ls /`

- Display a file's contents from a filesystem image:

`grub-fstest {{path/to/filesystem.img}} cat /boot/grub/grub.cfg`
