# deborphan

> Az árva csomagok megjelenítése az APT csomagkezelőt használó operációs rendszereken. További információ: <https://manpages.debian.org/latest/deborphan/deborphan.html>.

- Olyan könyvtárcsomagok megjelenítése (a csomagtár "libs" szakaszából), amelyekre egy másik csomagnak nincs szüksége:

`deborphan`

- A "libs" szakaszból származó árva csomagok, valamint az olyan árva csomagok listázása, amelyek neve könyvtárnévre hasonlít:

`deborphan --guess-all`

- Olyan csomagok keresése, amelyeket egy másik csomag csak ajánlott vagy javasolt (de nem szükséges):

`deborphan --nice-mode`
