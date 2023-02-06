# asciidoctor

> Egy olyan processzor, amely AsciiDoc fájlokat alakít át publikálható formátumba. További információ: <https://docs.asciidoctor.org>.

- Egy adott `.adoc` fájl átalakítása HTML formátumra (az alapértelmezett kimeneti formátum):

`asciidoctor {{path/to/file.adoc}}`

- Egy adott `.adoc` fájl átalakítása HTML-be és egy CSS stíluslap összekapcsolása:

`asciidoctor -a stylesheet={{path/to/stylesheet.css}} {{path/to/file.adoc}}`

- Egy adott `.adoc` fájl átalakítása beágyazható HTML-be, a test kivételével mindent eltávolítva:

`asciidoctor --embedded {{path/to/file.adoc}}`

- Egy adott `.adoc` fájl átalakítása PDF-be a `asciidoctor-pdf` könyvtár segítségével:

`asciidoctor --backend={{pdf}} --require={{asciidoctor-pdf}} {{path/to/file.adoc}}`
