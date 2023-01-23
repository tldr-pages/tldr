# tmutil

> Segédprogram a Time Machine biztonsági mentések kezeléséhez. A legtöbb ige root jogosultságokat igényel. További információ: <https://ss64.com/osx/tmutil.html>.

- HFS+ meghajtó beállítása a biztonsági mentés célpontjaként:

`sudo tmutil setdestination {{path/to/disk_mount_point}}`

- APF-megosztás vagy SMB-megosztás beállítása biztonsági mentés célpontjaként:

`sudo tmutil setdestination "{{protocol://user[:password]@host/share}}"`

- A megadott célállomás hozzáadása a célállomások listájához:

`sudo tmutil setdestination -a {{destination}}`

- Automatikus biztonsági mentések engedélyezése:

`sudo tmutil enable`

- Automatikus biztonsági mentések letiltása:

`sudo tmutil disable`

- Biztonsági mentés indítása, ha még nem fut, és a héj feletti irányítás felszabadítása:

`sudo tmutil startbackup`

- Biztonsági mentés indítása és blokkolás a mentés befejezéséig:

`sudo tmutil startbackup -b`

- Biztonsági mentés leállítása:

`sudo tmutil stopbackup`
