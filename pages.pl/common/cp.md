# cp

> Kopiuje pliki i katalogi.
> Więcej informacji: <https://www.gnu.org/software/coreutils/cp>.

- Kopiuj plik do innej lokalizacji:

`cp {{ścieżka/do/pliku_źródłowego.ext}} {{ścieżka/do/pliku_docelowego.ext}}`

- Kopiuj plik do innego katalogu, zachowując nazwę pliku:

`cp {{ścieżka/do/pliku_źródłowego}} {{ścieżka/do/katalogu}}`

- Kopiuj rekursywnie katalog z zawartością do innej lokalizacji (jeśli docelowa lokalizacja istnieje, katalog jest kopiowany do jej środka):

`cp -R {{ścieżka/do/katalogu_źródłowego}} {{ścieżka/do/katalogu_docelowego}}`

- Kopiuj katalog rekursywnie, w trybie opisowym (pokazuje pliki które zostały skopiowane):

`cp -vR {{ścieżka/do/katalogu_źródłowego}} {{ścieżka/do/katalogu_docelowego}}`

- Kopiuj pliki tekstowe do innej lokalizacji, w trybie interaktywnym (wyświetla pytanie o potwierdzenie przed nadpisywaniem):

`cp -i {{*.txt}} {{ścieżka/do/katalogu_docelowego}}`

- Podążaj za dowiązaniami symbolicznymi przed kopiowaniem:

`cp -L {{dowiązanie}} {{ścieżka/do/katalogu_docelowego}}`
