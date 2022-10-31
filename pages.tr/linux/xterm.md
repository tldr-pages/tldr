# xterm

> X Ekran Sistemi için terminal öykünücüsü.
> Daha fazla bilgi için: <https://manned.org/xterm>.

- `Örnek` başlığına sahip bir terminal aç:

`xterm -T {{Örnek}}`

- Terminali tam ekran modunda aç:

`xterm -fullscreen`

- Terminali lacivert arkaplan ve sarı ön plan (font rengi) ile aç:

`xterm -bg {{darkblue}} -fg {{yellow}}`

- Terminali satır başına 100 karakter ve sütun başına 35 satır sığacak şekilde, x=200px y=20px koordinatlarında aç:

`xterm -geometry {{100}}x{{35}}+{{200}}+{{20}}`

- Terminali bir Serif fontu ve 20'ye eşit olan bir font büyüklüğü ile aç:

`xterm -fa "{{Serif}}" -fs {{20}}`
