# lsusb

> Az USB-buszokról és a hozzájuk csatlakoztatott eszközökről szóló információk megjelenítése. További információk: <https://manned.org/lsusb>.

- Az összes rendelkezésre álló USB-eszköz felsorolása:

`lsusb`

- Az USB-hierarchia faként történő felsorolása:

`lsusb -t`

- Az USB-eszközökre vonatkozó szóbeli információk listázása:

`lsusb --verbose`

- Részletes információk listázása egy USB-eszközről:

`lsusb -D {{device}}`

- Csak a megadott gyártóval és termékazonosítóval rendelkező eszközök listázása:

`lsusb -d {{vendor}}:{{product}}`
