# losetup

> Hurokberendezések beállítása és vezérlése. További információ: <https://manned.org/losetup>.

- Hurokeszközök listája részletes információkkal:

`losetup -a`

- Fájl csatolása egy adott hurokeszközhöz:

`sudo losetup /dev/{{loop}} /{{path/to/file}}`

- Fájl csatolása egy új szabad hurokeszközhöz, és az eszköz átvizsgálása partíciók után:

`sudo losetup --show --partscan -f /{{path/to/file}}`

- Fájl csatolása egy csak olvasható hurokeszközhöz:

`sudo losetup --read-only /dev/{{loop}} /{{path/to/file}}`

- Az összes hurokeszköz leválasztása:

`sudo losetup -D`

- Egy adott hurokeszköz leválasztása:

`sudo losetup -d /dev/{{loop}}`
