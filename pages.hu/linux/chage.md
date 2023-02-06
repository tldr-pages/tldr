# chage

> A felhasználói fiók és a jelszó lejárati idejének módosítása. További információ: <https://manned.org/chage>.

- A felhasználó jelszóadatainak listázása:

`chage --list {{username}}`

- Engedélyezze a jelszó 10 napon belüli lejáratát:

`sudo chage --maxdays {{10}} {{username}}`

- Jelszó lejárati idejének letiltása:

`sudo chage --maxdays {{-1}} {{username}}`

- Fiók lejárati dátumának beállítása:

`sudo chage --expiredate {{YYYY-MM-DD}} {{username}}`

- Kényszerítse a felhasználót a jelszó megváltoztatására a következő bejelentkezéskor:

`sudo chage --lastday {{0}} {{username}}`
