# grub-bios-setup

> Egy eszköz beállítása a GRUB használatára BIOS-konfigurációval. A legtöbb esetben a `grub-bios-setup` helyett a `grub-install` címet kell használni. További információ: <https://manned.org/grub-bios-setup.8>.

- Állítson be egy eszközt a GRUB használatával történő indításra:

`grub-bios-setup {{/dev/sdX}}`

- Telepítse akkor is, ha problémákat észlel:

`grub-bios-setup --force {{/dev/sdX}}`

- Telepítse a GRUB-ot egy adott könyvtárba:

`grub-bios-setup --directory={{/boot/grub}} {{/dev/sdX}}`
