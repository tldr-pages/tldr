# robocopy

> Robusztus fájl- és mappamásolás. Alapértelmezés szerint a fájlok másolása csak akkor történik meg, ha a forrás és a célállomás eltérő időbélyegzővel vagy eltérő fájlmérettel rendelkezik. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy>.

- Az összes `.jpg` és `.bmp` fájl másolása egyik könyvtárból a másikba:

`robocopy {{path/to/source}} {{path/to/destination}} {{*.jpg}} {{*.bmp}}`

- Minden fájl és alkönyvtár másolása, beleértve az üres könyvtárakat is:

`robocopy {{path/to/source}} {{path/to/destination}} /E`

- Egy könyvtár tükrözése/szinkronizálása, törölve mindent, ami nincs a forrásban, és beleértve az összes attribútumot és engedélyt:

`robocopy {{path/to/source}} {{path/to/destination}} /MIR /COPYALL`

- Minden fájl és alkönyvtár másolása, kivéve a forrásfájlokat, amelyek régebbiek, mint a célfájlok:

`robocopy {{path/to/source}} {{path/to/destination}} /E /XO`

- Az összes 50 MB-os vagy annál nagyobb fájl listázása másolás helyett:

`robocopy {{path/to/source}} {{path/to/destination}} /MIN:{{52428800}} /L`

- Hálózati kapcsolat megszakadása esetén engedélyezze a folytatást, és korlátozza az újbóli próbálkozásokat 5-re, a várakozási időt pedig 15 másodpercre:

`robocopy {{path/to/source}} {{path/to/destination}} /Z /R:5 /W:15`

- Részletes használati információk megjelenítése:

`robocopy /?`
