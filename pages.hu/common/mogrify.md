# mogrify

> Több képen végezhet műveleteket, például méretváltoztatást, vágást, átfordítást és effektek hozzáadását. A módosítások közvetlenül az eredeti fájlra kerülnek alkalmazásra. További információ: <https://imagemagick.org/script/mogrify.php>.

- A könyvtárban lévő összes JPEG-kép méretének átméretezése az eredeti méretük 50%-ára:

`mogrify -resize {{50%}} {{*.jpg}}`

- A "DSC" betűvel kezdődő összes kép átméretezése 800x600-ra:

`mogrify -resize {{800x600}} {{DSC*}}`

- A könyvtárban található összes PNG képet JPEG formátumúvá alakítja:

`mogrify -format {{jpg}} {{*.png}}`

- Az aktuális könyvtárban lévő összes képfájl telítettségének felére csökkentése:

`mogrify -modulate {{100,50}} {{*}}`

- Az aktuális könyvtárban található összes képfájl fényerejének megduplázása:

`mogrify -modulate {{200}} {{*}}`
