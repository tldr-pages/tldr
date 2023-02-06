# kexec

> Közvetlen újraindítás új rendszermaggal. További információ: <https://manned.org/kexec>.

- Új rendszermag betöltése:

`kexec -l {{path/to/kernel}} --initrd={{path/to/initrd}} --command-line={{arguments}}`

- Új rendszermag betöltése az aktuális indítási paraméterekkel:

`kexec -l {{path/to/kernel}} --initrd={{path/to/initrd}} --reuse-cmdline`

- Az aktuálisan betöltött rendszermag végrehajtása:

`kexec -e`

- Az aktuális kexec célkernel kitöltésének megszüntetése:

`kexec -u`
