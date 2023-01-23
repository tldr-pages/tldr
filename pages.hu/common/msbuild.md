# msbuild

> A Microsoft építőeszköze a Visual Studio projektmegoldásokhoz. További információ: <https://learn.microsoft.com/visualstudio/msbuild>.

- Az aktuális könyvtárban lévő első projektfájl építése:

`msbuild`

- Egy adott projektfájl építése:

`msbuild {{path/to/project_file}}`

- Egy vagy több, pontosvesszővel elválasztott célpont beállítása a buildeléshez:

`msbuild {{path/to/project_file}} /target:{{targets}}`

- Egy vagy több, pontosvesszővel elválasztott tulajdonság beállítása:

`msbuild {{path/to/project_file}} /property:{{name=value}}`

- Beállítja a használandó build tools verziót:

`msbuild {{path/to/project_file}} /toolsversion:{{version}}`

- Részletes információk megjelenítése a napló végén a projekt konfigurálásáról:

`msbuild {{path/to/project_file}} /detailedsummary`

- Részletes súgóinformációk megjelenítése:

`msbuild /help`
