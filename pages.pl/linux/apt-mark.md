# apt-mark

> Narzędzie do zmiany statusu zainstalowanych pakietów.
> Więcej informacji: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Oznacz pakiet jako zainstalowany automatycznie:

`sudo apt-mark auto {{pakiet}}`

- Zatrzymaj pakiet w bieżącej wersji i zapobiegaj jego aktualizacjom:

`sudo apt-mark hold {{pakiet}}`

- Zezwól, aby pakiet znowu był aktualizowany:

`sudo apt-mark unhold {{pakiet}}`

- Pokaż pakiety zainstalowane ręcznie:

`apt-mark showmanual`

- Pokaż zatrzymane pakiety, które nie są aktualizowane:

`apt-mark showhold`
