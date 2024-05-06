# yaa

> Tworzenie archiwów YAA i manipulowanie nimi.
> Więcej informacji: <https://keith.github.io/xcode-man-pages/yaa.1.html>.

- Tworzenie archiwum z katalogu:

`yaa archive -d {{sciezka/do/katalogu}} -o {{sciezka/do/pliku_wyjscia.yaa}}`

- Tworzenie archiwum z pliku:

`yaa archive -i {{sciezka/do/pliku}} -o {{sciezka/do/pliku_wyjscia.yaa}}`

- Wypakowanie archiwum do obecnego folderu:

`yaa extract -i {{sciezka/do/pliku_archiwum.yaa}}`

- Lista zawartości archiwum:

`yaa list -i {{sciezka/do/pliku_archiwum.yaa}}`

- Tworzenie archiwum z określonym algorytmem kompresji:

`yaa archive -a {{algorytm}} -d {{sciezka/do/folderu}} -o {{sciezka/do/pliku_wyjscia.yaa}}`

- Utwórz archiwum o rozmiarze bloku 8 MB:

`yaa archive -b {{8m}} -d {{sciezka/do/folderu}} -o {{sciezka/do/pliku_wyjscia.yaa}}`
