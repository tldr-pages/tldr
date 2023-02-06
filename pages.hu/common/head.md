# head

> A fájlok első részének kimenete. További információ: <https://www.gnu.org/software/coreutils/head>.

- Egy fájl első néhány sorának kiadása:

`head --lines {{count}} {{path/to/file}}`

- Egy fájl első néhány bájtjának kiadása:

`head --bytes {{count}} {{path/to/file}}`

- Egy fájl utolsó néhány sorának kivételével mindent kiadni:

`head --lines -{{count}} {{path/to/file}}`

- A fájl utolsó néhány bájtján kívül mindent kiadni:

`head --bytes -{{count}} {{path/to/file}}`
