# ac

> Statisztikák nyomtatása arról, hogy a felhasználók mennyi ideig voltak kapcsolatban. További információ: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Kiírja, hogy az aktuális felhasználó mennyi ideje van kapcsolatban órákban kifejezve:

`ac`

- Nyomtassa ki, hogy a felhasználók mennyi ideje vannak kapcsolatban órákban kifejezve:

`ac --individual-totals`

- Kinyomtatja, hogy egy adott felhasználó mennyi ideig volt csatlakoztatva órákban:

`ac --individual-totals {{username}}`

- Nyomtassa ki, hogy egy adott felhasználó mennyi ideig volt csatlakoztatva naponta (összesen):

`ac --daily-totals --individual-totals {{username}}`

- További részletek megjelenítése:

`ac --compatibility`
