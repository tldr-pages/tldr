# size

> Displays the sizes of sections inside binary files.
> More information: <https://sourceware.org/binutils/docs/binutils/size.html>.

- Display the size of sections in a given object or executable file:

`size {{path/to/file}}`

- Display the size of sections in a given object or executable file in [o]ctal:

`size {{-o|--radix=8}} {{path/to/file}}`

- Display the size of sections in a given object or executable file in [d]ecimal:

`size {{-d|--radix=10}} {{path/to/file}}`

- Display the size of sections in a given object or executable file in he[x]adecimal:

`size {{-x|--radix=16}} {{path/to/file}}`
