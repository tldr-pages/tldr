# apt-file

> Wyszukaj pliki w pakietach APT, w tym jeszcze nie zainstalowanych.
> Więcej informacji: <https://manned.org/apt-file.1>.

- Zaktualizuj bazę metadanych:

`sudo apt update`

- Wyszukaj pakiet, który zawiera określony plik lub ścieżkę:

`apt-file {{search|find}} {{część/ścieżki/do/pliku}}`

- Wyświetl zawartośċ określonego pakietu:

`apt-file {{show|list}} {{pakiet}}`

- Wyszukaj pakiety, które pasują do podanego `wyrażenia_regularnego`:

`apt-file {{search|find}} {{[-x|--regexp]}} {{wyrażenie_regularne}}`
