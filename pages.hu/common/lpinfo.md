# lpinfo

> A csatlakoztatott nyomtatók és a CUPS nyomtatókiszolgálóhoz telepített illesztőprogramok listája. További információ: <https://www.cups.org/doc/man-lpinfo.html>.

- Az összes jelenleg csatlakoztatott nyomtató listázása:

`lpinfo -v`

- Az összes jelenleg telepített nyomtatóillesztő-program listája:

`lpinfo -m`

- A telepített nyomtatóillesztők keresése márka és modell alapján:

`lpinfo --make-and-model "{{printer_model}}" -m`
