# dphys-swapfile

> Manage the swap file on Debian-based Linux systems.
> More information: <https://manpages.debian.org/jessie/dphys-swapfile/dphys-swapfile.8.en.html>.

- Disable swap file:

`dphys-swapfile swapoff`

- Enable swap file:

`dphys-swapfile swapon`

- Create new swap file (e.g., after changes in file `/etc/dphys-swapfile `):

`dphys-swapfile setup`
