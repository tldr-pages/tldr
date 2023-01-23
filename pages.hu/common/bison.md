# bison

> GNU parser generátor. További információ: <https://www.gnu.org/software/bison/>.

- Kompiláljon egy bison definíciós fájlt:

`bison {{path/to/file.y}}`

- Fordítás hibakereső módban, ami azt eredményezi, hogy a kapott elemző további információkat ír a standard kimenetre:

`bison --debug {{path/to/file.y}}`

- Adja meg a kimeneti fájlnevet:

`bison --output {{path/to/output.c}} {{path/to/file.y}}`

- Legyen bőbeszédű a fordítás során:

`bison --verbose`
