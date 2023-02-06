# fdesetup

> A FileVault-tal kapcsolatos információk beállítása és lekérdezése. További információ: <https://www.unix.com/man-page/mojave/8/fdesetup/>.

- Az aktuális FileVault-engedélyezett felhasználók listája:

`sudo fdesetup list`

- A FileVault aktuális állapotának lekérdezése:

`fdesetup status`

- FileVault-képes felhasználó hozzáadása:

`sudo fdesetup add -usertoadd user1`

- FileVault engedélyezése:

`sudo fdesetup enable`

- FileVault letiltása:

`sudo fdesetup disable`
