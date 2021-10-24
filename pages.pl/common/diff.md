# diff

> Porównaj pliki i foldery.
> Więcej informacji: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Porównaj pliki (lista zmian między `stary_plik` a `nowy_plik`):

`diff {{stary_plik}} {{nowy_plik}}`

- Porównaj pliki, ignoruj białe znaki (white spaces):

`diff -w {{stary_plik}} {{nowy_plik}}`

- Porównaj pliki, pokaż różnice obok siebie:

`diff -y {{stary_plik}} {{nowy_plik}}`

- Porównaj pliki, pokaż różnice w ujednoliconym formacie (tak jak w przypadku `git diff`):

`diff -u {{stary_plik}} {{nowy_plik}}`

- Porównaj foldery rekurencyjnie (pokazuje nazwy różniących się plików/folderów a także zmiany w plikach):

`diff -r {{stary_folder}} {{nowy_folder}}`

- Porównaj foldery rekurencyjnie, pokaż tylko nazwy plików które się różnią:

`diff -rq {{stary_folder}} {{nowy_folder}}`
