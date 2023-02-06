# smbmap

> SMB enumerációs eszköz. További információ: <https://github.com/ShawnDEvans/smbmap>.

- SMB-megosztások és engedélyek megjelenítése egy állomáson, a felhasználó jelszavának vagy NTLM-hash-jének megadásával:

`smbmap -u {{username}} --prompt -H {{ip}}`

- SMB-megosztások és engedélyek megjelenítése egy állomáson, a tartomány megadásával és a jelszó NTLM hash átadásával:

`smbmap -u {{username}} --prompt -d {{domain}} -H {{ip}}`

- SMB-megosztások megjelenítése és a könyvtárak és fájlok egyetlen szintjének felsorolása:

`smbmap -u {{username}} --prompt -H {{ip}} -r`

- SMB-megosztások megjelenítése és a könyvtárak és fájlok meghatározott számú szintjének rekurzív listázása:

`smbmap -u {{username}} --prompt -H {{ip}} -R --depth {{3}}`

- SMB-megosztások megjelenítése és rekurzív listázása könyvtárak és fájlok listázása, a szabályos kifejezésnek megfelelő fájlok letöltése:

`smbmap -u {{username}} --prompt -H {{ip}} -R -A {{pattern}}`

- SMB-megosztások megjelenítése és könyvtárak és fájlok rekurzív listázása, a szabályos kifejezésnek megfelelő fájltartalom keresése:

`smbmap -u {{username}} --prompt -H {{ip}} -R -F {{pattern}}`

- Shell parancs végrehajtása egy távoli rendszeren:

`smbmap -u {{username}} --prompt -H {{ip}} -x {{command}}`

- Fájl feltöltése egy távoli rendszerre:

`smbmap -u {{username}} --prompt -H {{ip}} --upload {{source}} {{destination}}`
