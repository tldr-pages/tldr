# fls

> Fájlok és könyvtárak listázása egy képfájlban vagy eszközön. További információ: <https://wiki.sleuthkit.org/index.php?title=Fls>.

- Rekurzív fls lista készítése egy eszközön, a kimeneti elérési utak C-vel kezdődnek:

`fls -r -m {{C:}} {{/dev/loop1p1}}`

- Egyetlen partíció elemzése, megadva azt a szektoreltolódást, ahol a fájlrendszer a képen kezdődik:

`fls -r -m {{C:}} -o {{sector}} {{path/to/image_file}}`

- Elemezzen egyetlen partíciót, megadva az eredeti rendszer időzónáját:

`fls -r -m {{C:}} -z {{timezone}} {{/dev/loop1p1}}`
