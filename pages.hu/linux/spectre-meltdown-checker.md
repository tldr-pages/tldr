# spectre-meltdown-checker

> Spectre és Meltdown kockázatcsökkentő eszköz. További információ: <https://manned.org/spectre-meltdown-checker>.

- Ellenőrizze a jelenleg futó rendszermagot Spectre vagy Meltdown szempontjából:

`sudo spectre-meltdown-checker`

- Ellenőrizze a jelenleg futó rendszermagot, és mutassa meg a sebezhetőség mérséklésére irányuló lépések magyarázatát:

`sudo spectre-meltdown-checker --explain`

- Bizonyos változatok ellenőrzése (alapértelmezés szerint minden):

`sudo spectre-meltdown-checker --variant {{1|2|3|3a|4|l1tf|msbds|mfbds|mlpds|mdsum|taa|mcespc|srbds}}`

- Kimenet megjelenítése egy adott kimeneti formátumban:

`sudo spectre-meltdown-checker --batch {{text|json|nrpe|prometheus|short}}`

- Ne használja a `/sys` felületet még akkor sem, ha van:

`sudo spectre-meltdown-checker --no-sysfs`

- Ellenőrizze a nem futó rendszermagot:

`sudo spectre-meltdown-checker --kernel {{path/to/kernel_file}}`
