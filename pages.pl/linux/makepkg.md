# makepkg

> Utwórz pakiet do użycia przez `pacman`-a.
> Domyślnie używa pliku `PKGBUILD` w aktualnym katalogu roboczym.
> Więcej informacji: <https://manned.org/makepkg.8>.

- Utwórz pakiet:

`makepkg`

- Utwórz pakiet i zainstaluj jego zależności:

`makepkg {{[-s|--syncdeps]}}`

- Utwórz pakiet, zainstaluj jego zależności, a następnie zainstaluj utworzony pakiet:

`makepkg {{[-s|--syncdeps]}} {{[-i|--install]}}`

- Utwórz pakiet, ale pomiń sprawdzanie sum kontrolnych źrodeł:

`makepkg --skipchecksums`

- Wyczyść katalogi robocze po udanym budowaniu:

`makepkg {{[-c|--clean]}}`

- Zwerifikuj sumy kontrolne źródeł:

`makepkg --verifysource`

- Wygeneruj i zapisz informacje o źródłach do pliku `.SRCINFO`:

`makepkg --printsrcinfo > .SRCINFO`
