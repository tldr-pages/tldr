# rtcwake

> A rendszer alvó állapotba kerül a BIOS-órához viszonyított meghatározott ébresztési időpontig. További információ: <https://manned.org/rtcwake>.

- Megjeleníti, hogy van-e ébresztés beállítva vagy sem:

`sudo rtcwake -m show -v`

- Felfüggesztés a RAM-ba és ébresztés 10 másodperc múlva:

`sudo rtcwake -m mem -s {{10}}`

- Felfüggesztés lemezre (nagyobb energiatakarékosság) és ébresztés 15 perc múlva:

`sudo rtcwake -m disk --date +{{15}}min`

- A rendszer befagyasztása (hatékonyabb, mint a RAM-ra felfüggesztés, de a Linux kernel 3.9-es vagy újabb verziója szükséges) és ébredés egy megadott dátummal és időponttal:

`sudo rtcwake -m freeze --date {{YYYYMMDDhhmm}}`

- Egy korábban beállított riasztás letiltása:

`sudo rtcwake -m disable`

- Szárazfutás végrehajtása a számítógép adott időpontban történő felébresztéséhez. (A Ctrl + C billentyűkombinációval megszakíthatja a műveletet):

`sudo rtcwake -m on --date {{hh:ss}}`
