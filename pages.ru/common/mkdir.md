# mkdir

> Создание директорий и установка их прав доступа.
> Больше информации: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Создать указанные директории:

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- Создать указанные директории, включая родительские, при необходимости:

`mkdir {{[-p|--parents]}} {{path/to/directory1 path/to/directory2 ...}}`

- Создать директории с указанными правами доступа:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{path/to/directory1 path/to/directory2 ...}}`

- Создать несколько вложенных директорий рекурсивно:

`mkdir {{[-p|--parents]}} {{path/to/{a,b}/{x,y,z}/{h,i,j}}}`
