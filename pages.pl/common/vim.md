# vim

> Vim (Vi IMproved), edytor tekstu wiersza polecenia, oferuje kilka trybów dla różnych rodzajów manipulacji tekstem.
> Naciśnięcie przycisku `i` powoduje przejście do trybu edycji. `<Esc>` wraca do normalnego trybu, który nie pozwala na zwykłe wstawianie tekstu.
> Więcej informacji: <https://www.vim.org>.

- Otwórz plik:

`vim {{sciezka/do/plik}}`

- Otwórz plik pod określonym numerem wiersza:

`vim +{{numer_linii}} {{sciezka/do/plik}}`

- Zobacz instrukcję pomocy Vim:

`:help<Enter>`

- Zapisz plik:

`:write<Enter>`

- Wyjdź bez zapisywania:

`:quit!<Enter>`

- Cofnij ostatnią operację:

`u`

- Wyszukaj wzorzec w pliku (naciśnij `n`/`N` przejść do następnego/poprzedniego dopasowania):

`/{{szukaj_wzorca}}<Enter>`

- Wykonaj podstawienie wyrażenia regularnego w całym pliku:

`:%s/{{wzorzec}}/{{zastąpienie}}/g<Enter>`
