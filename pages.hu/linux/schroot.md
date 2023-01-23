# schroot

> Parancs futtatása vagy interaktív shell indítása egy másik gyökérkönyvtárral. Testreszabhatóbb, mint a `chroot`. További információ: <https://wiki.debian.org/Schroot>.

- Parancs futtatása egy adott chrootban:

`schroot --chroot {{chroot}} {{command}}`

- Parancs futtatása opciókkal egy adott chrootban:

`schroot --chroot {{chroot}} {{command}} -- {{command_options}}`

- Parancs futtatása az összes elérhető chrootban:

`schroot --all {{command}}`

- Interaktív shell indítása egy adott chrootban egy adott felhasználóval:

`schroot --chroot {{chroot}} --user {{user}}`

- Az elérhető chrootok listája:

`schroot --list`
