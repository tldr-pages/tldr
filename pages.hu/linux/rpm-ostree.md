# rpm-ostree

> Hibrid image/csomagrendszer. Ostree telepítések, csomagrétegek, fájlrendszer-áthelyezések és boot-konfigurációk kezelése. További információ: <https://coreos.github.io/rpm-ostree/administrator-handbook/>.

- Az rpm-ostree telepítések megjelenítése a bootloaderben megjelenő sorrendben:

`rpm-ostree status`

- Az elavult és frissíthető csomagok megjelenítése:

`rpm-ostree upgrade --preview`

- Készítsen elő egy új ostree telepítést frissített csomagokkal, és indítsa újra:

`rpm-ostree upgrade --reboot`

- Újraindítás az előző ostree telepítésbe:

`rpm-ostree rollback --reboot`

- Telepítsen egy csomagot egy új ostree telepítésbe, és indítsa újra azt:

`rpm-ostree install {{package}} --reboot`
