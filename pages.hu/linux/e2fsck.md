# e2fsck

> Ellenőrizzen egy Linux ext2/ext3/ext4 fájlrendszert. A partíciót le kell csatolni. További információ: <https://manned.org/e2fsck>.

- Ellenőrizze a fájlrendszert, jelentse a sérült blokkokat:

`sudo e2fsck {{/dev/sdXN}}`

- A fájlrendszer ellenőrzése és a sérült blokkok automatikus javítása:

`sudo e2fsck -p {{/dev/sdXN}}`

- Csak olvasási módban lévő fájlrendszer ellenőrzése:

`sudo e2fsck -c {{/dev/sdXN}}`

- Kimerítő, roncsolásmentes író-olvasó teszt elvégzése a rossz blokkok keresésére és feketelistára helyezésük:

`sudo e2fsck -fccky {{/dev/sdXN}}`
