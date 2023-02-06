# csrutil

> A System Integrity Protection konfiguráció kezelése. További információ: <https://ss64.com/osx/csrutil.html>.

- A rendszer integritásvédelmi állapot megjelenítése:

`csrutil status`

- A rendszerintegritás-védelem letiltása:

`csrutil disable`

- A rendszer integritásvédelmének engedélyezése:

`csrutil enable`

- Az engedélyezett NetBoot-források listájának megjelenítése:

`csrutil netboot list`

- IPv4-cím hozzáadása az engedélyezett NetBoot-források listájához:

`csrutil netboot add {{ip_address}}`

- A rendszer integritásvédelmi állapot visszaállítása és a NetBoot-lista törlése:

`csrutil clear`
