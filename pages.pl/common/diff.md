# diff

> Porównaj pliki i foldery.
> Więcej informacji: <https://manned.org/diff>.

- Porównaj pliki (lista zmian między `stary_plik` a `nowy_plik`):

`diff {{stary_plik}} {{nowy_plik}}`

- Porównaj pliki, ignoruj białe znaki (white spaces):

`diff {{[-w|--ignore-all-space]}} {{stary_plik}} {{nowy_plik}}`

- Porównaj pliki, pokaż różnice obok siebie:

`diff {{[-y|--side-by-side]}} {{stary_plik}} {{nowy_plik}}`

- Porównaj pliki, pokaż różnice w ujednoliconym formacie (tak jak w przypadku `git diff`):

`diff {{[-u|--unified]}} {{stary_plik}} {{nowy_plik}}`

- Porównaj foldery rekurencyjnie (pokazuje nazwy różniących się plików/folderów a także zmiany w plikach):

`diff {{[-r|--recursive]}} {{stary_folder}} {{nowy_folder}}`

- Porównaj foldery rekurencyjnie, pokaż tylko nazwy plików które się różnią:

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{stary_folder}} {{nowy_folder}}`
