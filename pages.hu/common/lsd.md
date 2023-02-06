# lsd

> List directory contents. A következő generációs `ls` parancs, Rust nyelven írva. További információ: <https://github.com/Peltoche/lsd>.

- Fájlok és könyvtárak listázása, soronként egyenként:

`lsd -1`

- Az aktuális könyvtárban lévő összes fájl és könyvtár listázása, beleértve a rejtetteket is:

`lsd -a`

- List all files and directories with trailing `/` added to directory names:

`lsd -F`

- Az összes fájl és könyvtár listázása hosszú formátumban (jogosultságok, tulajdonjog, méret és módosítási dátum):

`lsd -la`

- Az összes fájl és könyvtár hosszú formátumban történő felsorolása, a méret emberi olvasásra alkalmas egységekben (KiB, MiB, GiB) történő megjelenítésével:

`lsd -lh`

- Az összes fájl és könyvtár hosszú formátumban, méret szerint rendezve (csökkenő):

`lsd -lS`

- Az összes fájl és könyvtár hosszú formátumban, a módosítás dátuma szerint rendezve (a legrégebbi előbbre):

`lsd -ltr`

- Csak könyvtárak listázása:

`lsd -d {{*/}}`
