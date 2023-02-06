# join

> Két rendezett fájl sorainak összekapcsolása egy közös mezőn. További információ: <https://www.gnu.org/software/coreutils/join>.

- Két fájl egyesítése az első (alapértelmezett) mezőn:

`join {{file1}} {{file2}}`

- Két fájl összekapcsolása vesszővel (szóköz helyett) mint mezőelválasztóval:

`join -t {{','}} {{file1}} {{file2}}`

- Join field3 of file1 of file1 with field1 of file2:

`join -1 {{3}} -2 {{1}} {{file1}} {{file2}}`

- Készítsen egy sort minden egyes nem párosítható sorhoz a file1 számára:

`join -a {{1}} {{file1}} {{file2}}`

- Csatlakoztasson egy fájlt a `stdin`:

`cat {{path/to/file1}} | join - {{path/to/file2}}`
