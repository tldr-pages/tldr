# enum4linux

> Eszköz a Windows és Samba információk számbavételére távoli rendszerekről. További információ: <https://labs.portcullis.co.uk/tools/enum4linux/>.

- Próbálja meg az összes módszerrel elvégezni a felsorolást:

`enum4linux -a {{remote_host}}`

- Számbavétel a megadott bejelentkezési adatokkal:

`enum4linux -u {{user_name}} -p {{password}} {{remote_host}}`

- Felhasználónevek listázása egy adott állomásról:

`enum4linux -U {{remote_host}}`

- Megosztások listázása:

`enum4linux -S {{remote_host}}`

- Operációs rendszer információinak lekérdezése:

`enum4linux -o {{remote_host}}`
