# xcopy

> Kopiuje pliki i katalogi, w tym podkatalogi.
> Więcej informacji: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Skopiuj plik(i) do określonego miejsca docelowego:

`xcopy {{ścieżka/do/pliku_lub_katalogu}} {{ścieżka/do/miejsca_przeznaczenia}}`

- Wyświetl listę plików, które zostaną skopiowane przed skopiowaniem:

`xcopy {{ścieżka/do/pliku_lub_katalogu}} {{ścieżka/do/miejsca_przeznaczenia}} /p`

- Skopiuj tylko strukturę katalogów, z wyłączeniem plików:

`xcopy {{ścieżka/do/pliku_lub_katalogu}} {{ścieżka/do/miejsca_przeznaczenia}} /t`

- Dołącz puste katalogi podczas kopiowania:

`xcopy {{ścieżka/do/pliku_lub_katalogu}} {{ścieżka/do/miejsca_przeznaczenia}} /e`

- Zachowaj źródłową listę ACL w miejscu docelowym:

`xcopy {{ścieżka/do/pliku_lub_katalogu}} {{ścieżka/do/miejsca_przeznaczenia}} /o`

- Zezwól na wznawianie po utracie połączenia sieciowego:

`xcopy {{ścieżka/do/pliku_lub_katalogu}} {{ścieżka/do/miejsca_przeznaczenia}} /z`

- Wyłącz monit, gdy plik istnieje w miejscu docelowym:

`xcopy {{ścieżka/do/pliku_lub_katalogu}} {{ścieżka/do/miejsca_przeznaczenia}} /y`

- Wyświetl szczegółowe informacje dotyczące polecenia:

`xcopy /?`
