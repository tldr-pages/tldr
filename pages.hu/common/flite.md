# flite

> Beszédszintetizáló motor. További információ: <http://www.festvox.org/flite/doc/>.

- Az összes rendelkezésre álló hang listája:

`flite -lv`

- Szöveges karakterlánc beszéddé alakítása:

`flite -t "{{string}}"`

- Egy fájl tartalmának beszéddé alakítása:

`flite -f {{path/to/file.txt}}`

- A használandó hang megadása:

`flite -voice {{file://path/to/filename.flitevox|url}}`

- A kimenet wav fájlba történő tárolása:

`flite -voice {{file://path/to/filename.flitevox|url}} -f {{path/to/file.txt}} -o {{output.wav}}`

- Verzió megjelenítése:

`flite --version`
