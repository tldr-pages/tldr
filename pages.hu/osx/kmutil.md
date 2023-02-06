# kmutil

> Segédprogram a kernel kiterjesztések (kexts) és kext gyűjtemények kezelésére a lemezen. További információ: <https://keith.github.io/xcode-man-pages/kmutil.8.html>.

- Az operációs rendszerben elérhető kexts keresése:

`kmutil find`

- Naplózási információk megjelenítése a Kernel Management alrendszerről:

`kmutil log`

- A kextgyűjtemény tartalmának vizsgálata és megjelenítése a megadott beállítások szerint:

`kmutil inspect {{options}}`

- A kextgyűjtemények konzisztenciájának ellenőrzése egymással szemben:

`kmutil check`

- A kernelmanagerd állapotának kiürítése hibakeresés céljából:

`sudo kmutil dumpstate`

- Egy vagy több bővítmény betöltése az eredményekben megadott elérési útvonalon megadott csomag alapján:

`kmutil load --bundle-path {{path/to/extension.kext}}`
