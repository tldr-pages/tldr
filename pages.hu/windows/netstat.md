# netstat

> Megjeleníti az aktív TCP-kapcsolatokat, a számítógép által figyelt portokat, a hálózati adapterek statisztikáit, az IP-útválasztási táblázatot, az IPv4- és IPv6-statisztikákat. További információk: <https://learn.microsoft.com/windows-server/administration/windows-commands/netstat>.

- Aktív TCP-kapcsolatok megjelenítése:

`netstat`

- Megjeleníti az összes aktív TCP-kapcsolatot, valamint azokat a TCP- és UDP-portokat, amelyeken a számítógép hallgat:

`netstat -a`

- Hálózati adapter statisztikák megjelenítése, például az elküldött és fogadott bájtok és csomagok száma:

`netstat -e`

- Az aktív TCP-kapcsolatok, valamint a kifejezett címek és portszámok numerikus megjelenítése:

`netstat -n`

- Az aktív TCP-kapcsolatok megjelenítése, és minden kapcsolathoz a folyamatazonosító (PID) feltüntetése:

`netstat -o`

- Az IP útválasztási táblázat tartalmának megjelenítése:

`netstat -r`

- Statisztikák megjelenítése protokollok szerint:

`netstat -s`

- A jelenleg nyitott portok és a hozzájuk tartozó IP-címek listájának megjelenítése:

`netstat -an`
