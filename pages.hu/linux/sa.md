# sa

> Összefoglalja a számviteli információkat. Az acct csomag része. Megmutatja a felhasználók által hívott parancsokat, beleértve a feldolgozásra fordított CPU-időre és az I/O sebességre vonatkozó alapvető információkat. További információ: <https://manned.org/man/sa.8>.

- Felhasználónként megjeleníti a futtatható meghívásokat (a felhasználónév nem jelenik meg):

`sudo sa`

- A futtatható hívások megjelenítése felhasználónként, a felelős felhasználónevek feltüntetésével:

`sudo sa --print-users`

- A nemrégiben használt erőforrások listája felhasználónként:

`sudo sa --user-summary`
