# apt-file

> Wyszukiwanie plików w pakietach apt, łącznie z tymi jeszcze nie zainstalowanymi.
> Więcej informacji: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Aktualizacja bazy metadanych:

`sudo apt update`

- Wyszukanie pakietu, który zawiera określony plik lub ścieżkę:

`apt-file {{search|find}} {{część/ścieżki/do/pliku}}`

- Wyświetlenie zawartości określonego pakietu:

`apt-file {{show|list}} {{pakiet}}`

- Wyszukanie pakietów, które pasują do podanego `wyrażenia_regularnego`:

`apt-file {{search|find}} --regexp {{wyrażenie_regularne}}`
