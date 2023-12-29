# vim

> Vim (Vi IMproved), edytor tekstu wiersza polecenia, oferuje kilka trybów dla różnych rodzajów manipulacji tekstem.
> Naciśnięcie `i` powoduje przejście do trybu edycji. `<Esc>` wraca do normalnego trybu, który pozwala na używanie komend.
> Więcej informacji: <https://www.vim.org>.

- Otwórz plik:

`vim {{scieżka/do/pliku}}`

- Otwórz plik pod określonym numerem wiersza:

`vim +{{numer_linii}} {{scieżka/do/pliku}}`

- Zobacz instrukcję pomocy Vim:

`:help<Enter>`

- Wyjdź bez zapisywania:

`:wq<Enter>`

- Cofnij ostatnią operację:

`<Esc>u`

- Wyszukaj wzorzec w pliku (naciśnij `n`/`N` przejść do następnego/poprzedniego dopasowania):

`/{{szukaj_wzorca}}<Enter>`

- Wykonaj podstawienie wyrażenia regularnego w całym pliku:

`:%s/{{wzorzec}}/{{zastąpienie}}/g<Enter>`

- Wyświetlaj numery linii:

`:set nu<Enter>`
