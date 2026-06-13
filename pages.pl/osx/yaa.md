# yaa

> Twórz i manipuluj archiwami YAA.
> Więcej informacji: <https://www.manpagez.com/man/1/yaa/>.

- Utwórz archiwum z katalogu:

`yaa archive -d {{ścieżka/do/katalogu}} -o {{ścieżka/do/pliku_wyjścia.yaa}}`

- Utwórz archiwum z pliku:

`yaa archive -i {{ścieżka/do/pliku}} -o {{ścieżka/do/pliku_wyjścia.yaa}}`

- Wypakuj archiwum do obecnego folderu:

`yaa extract -i {{ścieżka/do/pliku_archiwum.yaa}}`

- Wyświetl zawartość archiwum:

`yaa list -i {{ścieżka/do/pliku_archiwum.yaa}}`

- Utwórz archiwum z określonym algorytmem kompresji:

`yaa archive -a {{algorytm}} -d {{ścieżka/do/folderu}} -o {{ścieżka/do/pliku_wyjścia.yaa}}`

- Utwórz archiwum o rozmiarze bloku 8 MB:

`yaa archive -b 8m -d {{ścieżka/do/folderu}} -o {{ścieżka/do/pliku_wyjścia.yaa}}`
