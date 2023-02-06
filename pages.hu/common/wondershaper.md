# wondershaper

> Lehetővé teszi a felhasználó számára egy vagy több hálózati adapter sávszélességének korlátozását. További információ: <https://github.com/magnific0/wondershaper#usage>.

- Display \[h\]elp:

`wondershaper -h`

- Megjeleníti egy adott \[a\]dapter aktuális \[s\]állapotát:

`wondershaper -s -a {{adapter_name}}`

- Korlátok törlése egy adott \[a\]dapterről:

`wondershaper -c -a {{adapter_name}}`

- Egy adott maximális \[d\]saját terhelési sebesség beállítása (Kbps-ban):

`wondershaper -a {{adapter_name}} -d {{1024}}`

- Egy adott maximális \[u\]pload rate (Kbps-ban) beállítása:

`wondershaper -a {{adapter_name}} -u {{512}}`

- Egy adott maximális \[d\]saját terhelési sebesség és \[u\]terhelési sebesség (Kpbs-ben) beállítása:

`wondershaper -a {{adapter_name}} -d {{1024}} -u {{512}}`
