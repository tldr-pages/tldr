# apt-cache

> Narzędzie do zapytań o pakiety w Debianie i Ubuntu.
> Więcej informacji: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Wyszukaj pakiet w aktualnych źródłach:

`apt-cache search {{zapytanie}}`

- Wyświetl informacje o pakiecie:

`apt-cache show {{pakiet}}`

- Wyświetl, czy pakiet jest zainstalowany w aktualnej wersji:

`apt-cache policy {{pakiet}}`

- Wyświetl zależności pakietu:

`apt-cache depends {{pakiet}}`

- Wyświetl pakiety zależne od konkretnego pakietu:

`apt-cache rdepends {{pakiet}}`
