# arch-chroot

> Továbbfejlesztett `chroot` parancs, amely segít az Arch Linux telepítési folyamatában. További információ: <https://man.archlinux.org/man/arch-chroot.8>.

- Indítson el egy interaktív héjat (`bash`, alapértelmezés szerint) egy új gyökérkönyvtárban:

`arch-chroot {{path/to/new/root}}`

- Adja meg azt a felhasználót (az aktuális felhasználótól eltérő), akinek a nevén a héj futni fog:

`arch-chroot -u {{user}} {{path/to/new/root}}`

- Egyéni parancs futtatása (az alapértelmezett `bash` helyett) az új gyökérkönyvtárban:

`arch-chroot {{path/to/new/root}} {{command}} {{command_arguments}}`

- Adja meg az alapértelmezett `bash` -tól eltérő parancsértelmező héjat (ebben az esetben a `zsh` csomagnak telepítve kell lennie a célrendszerben):

`arch-chroot {{path/to/new/root}} {{zsh}}`
