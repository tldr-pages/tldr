# od

> A fájl tartalmának megjelenítése oktális, decimális vagy hexadecimális formátumban. Opcionálisan megjelenítheti az egyes sorok bájteltolását és/vagy nyomtatható ábrázolását. További információ: <https://www.gnu.org/software/coreutils/od>.

- A fájl megjelenítése alapértelmezett beállításokkal: oktális formátum, 8 bájt soronként, bájteltolódások oktálisan, és a duplikált sorok helyettesítése `*`:

`od {{path/to/file}}`

- A fájl megjelenítése bőbeszédű üzemmódban, azaz a duplikált sorok `*`-val történő helyettesítése nélkül:

`od -v {{path/to/file}}`

- A fájl megjelenítése hexadecimális formátumban (2 bájtos egységek), bájteltolódásokkal decimális formátumban:

`od --format={{x}} --address-radix={{d}} -v {{path/to/file}}`

- A fájl megjelenítése hexadecimális formátumban (1 bájtos egységekben), soronként 4 bájttal:

`od --format={{x1}} --width={{4}} -v {{path/to/file}}`

- A fájl megjelenítése hexadecimális formátumban, a karakteres ábrázolással együtt, és nem írja ki a bájteltolásokat:

`od --format={{xz}} --address-radix={{n}} -v {{path/to/file}}`

- A fájlból csak 100 bájtot olvas be az 500. bájttól kezdve:

`od --read-bytes {{100}} --skip-bytes={{500}} -v {{path/to/file}}`
