# apt-file

> Wyszukaj pliki w pakietach APT, w tym jeszcze nie zainstalowanych.
> Więcej informacji: <https://manned.org/apt-file>.

- Zaktualizuj bazę metadanych:

`sudo apt update`

- Wyszukaj pakiet, który zawiera określony plik lub ścieżkę:

`apt-file {{[find|search]}} {{część/ścieżki/do/pliku}}`

- Wyświetl zawartośċ określonego pakietu:

`apt-file list {{pakiet}}`

- Wyszukaj pakiety, które pasują do podanego `wyrażenia_regularnego`:

`apt-file {{[find|search]}} {{[-x|--regexp]}} {{wyrażenie_regularne}}`
