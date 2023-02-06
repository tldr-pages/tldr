# runsvdir

> A szolgáltatások teljes könyvtárának futtatása. További információ: <https://manpages.ubuntu.com/manpages/latest/man8/runsvdir.8.html>.

- Egy könyvtár összes szolgáltatásának elindítása és kezelése az aktuális felhasználóként:

`runsvdir {{path/to/services}}`

- Egy könyvtár összes szolgáltatásának elindítása és kezelése root felhasználóként:

`sudo runsvdir {{path/to/services}}`

- A szolgáltatások külön munkamenetben történő indítása:

`runsvdir -P {{path/to/services}}`
