# setfacl

> Fájl-hozzáférésvezérlési listák (ACL) beállítása. További információ: <https://manned.org/setfacl>.

- Egy fájl ACL-jének módosítása olvasási és írási hozzáféréssel rendelkező felhasználók számára:

`setfacl -m u:{{username}}:rw {{file}}`

- A fájl alapértelmezett ACL-jének módosítása minden felhasználó számára:

`setfacl -d -m u::rw {{file}}`

- Egy fájl ACL-jének eltávolítása egy felhasználó számára:

`setfacl -x u:{{username}} {{file}}`

- Egy fájl összes ACL-bejegyzésének eltávolítása:

`setfacl -b {{file}}`
