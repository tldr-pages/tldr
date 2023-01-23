# doas

> Parancsot hajt végre egy másik felhasználóként. További információ: <https://man.openbsd.org/doas>.

- Parancs futtatása root felhasználóként:

`doas {{command}}`

- Parancs futtatása egy másik felhasználóként:

`doas -u {{user}} {{command}}`

- Az alapértelmezett shell indítása root felhasználóként:

`doas -s`

- Konfigurációs fájl elemzése és annak ellenőrzése, hogy egy parancs más felhasználóként történő végrehajtása engedélyezett-e:

`doas -C {{config_file}} {{command}}`

- A `doas` kérjen jelszót a korábban megadott jelszó után is:

`doas -L`
