# etckeeper

> Rendszerkonfigurációs fájlok nyomon követése a Gitben. További információ: <http://etckeeper.branchable.com/>.

- Git repo beállítása és különböző beállítási feladatok elvégzése (futtatható a `/etc` oldalon):

`sudo etckeeper init`

- Minden változtatás commitolása a `/etc`:

`sudo etckeeper commit {{message}}`

- Tetszőleges Git parancsok futtatása:

`sudo etckeeper vcs {{status}}`

- Ellenőrizze, hogy vannak-e nem commitolt változtatások (csak kilépési kódot ad vissza):

`sudo etckeeper unclean`

- A meglévő repo megsemmisítése és a változások követésének leállítása:

`sudo etckeeper uninit`
