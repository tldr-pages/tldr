# apt-cache

> Narzędzie do zapytań o pakiety w Debianie i Ubuntu.
> Więcej informacji: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Wyszukanie pakietu w aktualnych źródłach:

`apt-cache search {{zapytanie}}`

- Pokazanie informacji o pakiecie:

`apt-cache show {{pakiet}}`

- Pokazanie, czy pakiet jest zainstalowany i aktualnej wersji:

`apt-cache policy {{pakiet}}`

- Pokazanie zależności pakietu:

`apt-cache depends {{pakiet}}`

- Pokazanie pakietów mających zależność od konkretnego pakietu:

`apt-cache rdepends {{pakiet}}`
