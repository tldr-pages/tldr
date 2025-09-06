# ls

> Wypisz zawartość katalogu.
> Więcej informacji: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Wypisz po jednym pliku w linijce:

`ls -1`

- Wypisz wszystkie pliki, w tym ukryte:

`ls {{[-a|--all]}}`

- Wypisz wszystkie pliki z `/` na końcu nazw katalogów:

`ls {{[-F|--classify]}}`

- Wypisz listę w długim formacie (uprawnienia, własność, rozmiar i data modyfikacji) wszystkich plików:

`ls {{[-la|--all -l]}}`

- Wypisz listę w długim formacie z rozmiarem w jednostkach z przedrostkami dwójkowymi (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Wypisz listę rekurencyjnie w długim formacie, posortowaną po rozmiarze (malejąco):

`ls {{-lSR|-lS --recursive}}`

- Wypisz listę wszystkich plików w długim formacie posortowaną według daty modyfikacji (od najstarszych):

`ls {{[-ltr|-lt --reverse]}}`

- Wypisz tylko katalogi:

`ls {{[-d|--directory]}} */`
