# ls

> A könyvtár tartalmának listázása. További információ: <https://www.gnu.org/software/coreutils/ls>.

- Fájlok soronkénti felsorolása:

`ls -1`

- Az összes fájl listázása, beleértve a rejtett fájlokat is:

`ls -a`

- List all files, a könyvtárnevekhez hozzáadva a `/` utótagot:

`ls -F`

- Az összes fájl hosszú formátumú listája (engedélyek, tulajdonjog, méret és módosítási dátum):

`ls -la`

- Hosszú formátumú lista, a méret megjelenítése ember által olvasható egységekben (KiB, MiB, GiB):

`ls -lh`

- Hosszú formátumú lista méret szerint rendezve (csökkenő):

`ls -lS`

- Hosszú formátumú lista az összes fájlról, módosítási dátum szerint rendezve (a legrégebbi előbbre):

`ls -ltr`

- Csak könyvtárak listája:

`ls -d */`
