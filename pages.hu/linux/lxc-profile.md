# lxc profile

> Az LXD konténerek profiljainak kezelése. További információ: <https://linuxcontainers.org/lxd/docs/master/profiles>.

- Az összes elérhető profil listázása:

`lxc profile list`

- Egy adott profil konfigurációjának megjelenítése:

`lxc profile show {{profile_name}}`

- Egy adott profil szerkesztése az alapértelmezett szerkesztőprogramban:

`lxc profile edit {{profile_name}}`

- Egy adott profil szerkesztése a konfigurációs értékek importálásával egy fájlból:

`lxc profile edit {{profile_name}} < {{config.yaml}}`

- Új konténer indítása meghatározott profilokkal:

`lxc launch {{container_image}} {{container_name}} --profile {{profile1}} --profile {{profile2}}`

- Egy futó konténer profiljainak módosítása:

`lxc profile assign {{container_name}} {{profile1,profile2}}`
