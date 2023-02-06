# mkinitcpio

> A Linux kernel indításához szükséges kezdeti ramdisk környezeteket generál a megadott előbeállítás(ok) alapján. További információ: <https://man.archlinux.org/man/mkinitcpio.8>.

- Száraz futtatás elvégzése (nyomtassa ki, hogy mit csinálna anélkül, hogy ténylegesen meg is tenné):

`mkinitcpio`

- Generál egy ramdisk környezetet a `linux` előbeállítás alapján:

`mkinitcpio --preset {{linux}}`

- Ramdisk környezet létrehozása a `linux-lts` előbeállítás alapján:

`mkinitcpio --preset {{linux-lts}}`

- Az összes létező preset alapján ramdisk környezetek generálása (a `/etc/mkinitcpio.conf` megváltoztatása után az összes initramfs kép újratermelésére szolgál):

`mkinitcpio --allpresets`

- Initramfs-kép generálása egy alternatív konfigurációs fájl segítségével:

`mkinitcpio --config {{path/to/mkinitcpio.conf}} --generate {{path/to/initramfs.img}}`

- Initramfs-kép generálása a jelenleg futó kerneltől eltérő kernelhez (a telepített kernelkiadások a `/usr/lib/modules/` oldalon találhatók):

`mkinitcpio --kernel {{kernel_version}} --generate {{path/to/initramfs.img}}`

- Az összes rendelkezésre álló horgok listája:

`mkinitcpio --listhooks`

- Egy adott kampóhoz tartozó súgó megjelenítése:

`mkinitcpio --hookhelp {{hook_name}}`
