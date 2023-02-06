# hdparm

> SATA és IDE merevlemezek paramétereinek lekérdezése és beállítása. További információ: <https://manned.org/hdparm>.

- Egy adott eszköz azonosító adatainak lekérdezése:

`sudo hdparm -I /dev/{{device}}`

- A fejlett energiagazdálkodási szint lekérdezése:

`sudo hdparm -B /dev/{{device}}`

- A Speciális energiagazdálkodás értékének beállítása (az 1-127-es értékek engedélyezik a lekapcsolást, a 128-254-es értékek pedig nem):

`sudo hdparm -B {{1}} /dev/{{device}}`

- Megjeleníti az eszköz aktuális energiaellátási üzemmódjának állapotát:

`sudo hdparm -C /dev/{{device}}`

- A meghajtó azonnali készenléti üzemmódra kényszerítése (általában a meghajtó leállítását okozza):

`sudo hdparm -y /dev/{{device}}`

- A meghajtót üresjárati (alacsony fogyasztású) üzemmódba helyezi, beállítva a készenléti időhatárt is:

`sudo hdparm -S {{standby_timeout}} {{device}}`

- Egy adott eszköz olvasási sebességének tesztelése:

`sudo hdparm -tT {{device}}`
