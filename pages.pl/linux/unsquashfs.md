# unsquashfs

> Dekompresuj, rozpakuj i wyświetl listę plików w systemach plików squashfs.
> Więcej informacji: <https://manned.org/unsquashfs>.

- Rozpakuj system plików squashfs do `squashfs-root` w aktualnym katalogu roboczym:

`unsquashfs {{system_plików.squashfs}}`

- Rozpakuj system plików squashfs do podanego katalogu:

`unsquashfs {{[-d|-dest]}} {{ścieżka/do/katalogu}} {{system_plików.squashfs}}`

- Wyświetlaj nazwy plików podczas ich rozpakowywania:

`unsquashfs {{[-i|-info]}} {{system_plików.squashfs}}`

- Wyświetlaj nazwy plików i ich atrybuty podczas ich rozpakowywania:

`unsquashfs {{[-li|-linfo]}} {{system_plików.squashfs}}`

- Wyświetl listę plików w systemie plików squashfs (bez rozpakowywania):

`unsquashfs {{[-l|-ls]}} {{system_plików.squashfs}}`

- Wyświetl listę plików i ich atrybuty w systemie plików squashfs (bez rozpakowywania):

`unsquashfs {{[-ll|-lls]}} {{system_plików.squashfs}}`
