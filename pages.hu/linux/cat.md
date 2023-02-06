# cat

> Fájlok nyomtatása és összekapcsolása. További információ: <https://www.gnu.org/software/coreutils/cat>.

- Egy fájl tartalmának kinyomtatása a szabványos kimenetre:

`cat {{path/to/file}}`

- Több fájl összevonása egy kimeneti fájlba:

`cat {{path/to/file1 path/to/file2 ...}} > {{path/to/output_file}}`

- Több fájl csatolása egy kimeneti fájlhoz:

`cat {{path/to/file1 path/to/file2 ...}} >> {{path/to/output_file}}`

- Egy fájl tartalmának másolása egy kimeneti fájlba \[u\]nbuffered módban:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- `stdin` írása egy fájlba:

`cat - > {{path/to/file}}`

- \[n\]umber minden kimeneti sor:

`cat -n {{path/to/file}}`

- Nem nyomtatható és szóköz karakterek megjelenítése ( `M-` előtaggal, ha nem ASCII):

`cat -v -t -e {{path/to/file}}`
