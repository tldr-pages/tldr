# grub-mkconfig

> GRUB konfigurációs fájl létrehozása. További információ: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dmkconfig.html>.

- Végezzen egy próbafuttatást, és nyomtassa ki a konfigurációt a `stdout` címre:

`sudo grub-mkconfig`

- Generálja a konfigurációs fájlt:

`sudo grub-mkconfig --output={{/boot/grub/grub.cfg}}`

- Nyomtassa ki a súgóoldalt:

`grub-mkconfig --help`
