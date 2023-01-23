# faillock

> Hitelesítési hiba rekordfájlok megjelenítése és módosítása. További információ: <https://manned.org/faillock>.

- Az összes felhasználó bejelentkezési hibáinak listázása:

`sudo faillock`

- A megadott felhasználó bejelentkezési hibáinak listázása:

`sudo faillock --user {{user}}`

- A megadott felhasználó hiba rekordjainak visszaállítása:

`sudo faillock --user {{user}} --reset`
