# physlock

> Zárolja az összes konzolt és virtuális terminált. További információ: <http://github.com/muennich/physlock>.

- Minden konzol zárolása (a zárolás feloldásához az aktuális felhasználónak vagy a root rendszergazdának kell lennie):

`physlock`

- A konzolon megjelenő kernelüzenetek elnémítása zárolás közben:

`physlock -m`

- A SysRq mechanizmus letiltása zárolás közben:

`physlock -s`

- Üzenet megjelenítése a jelszavas kérés előtt:

`physlock -p "{{Locked!}}"`

- Fork és detach physlock (hasznos felfüggesztési vagy hibernációs szkriptekhez):

`physlock -d`
