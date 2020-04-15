# vim

> Vim (Vi IMproved), edytor tekstu wiersza polecenia, oferuje kilka trybów dla różnych rodzajów manipulacji tekstem.
> Naciśnięcie przycisku `i` powoduje przejście do trybu edycji. `<Esc>` wraca do normalnego trybu, który nie pozwala na zwykłe wstawianie tekstu.
> Więcej informacji: <https://www.vim.org>.

- Otwórz plik:

`vim {{path/to/file}}`

- Zobacz instrukcję pomocy Vim:

`:help<Enter>`

- Zapisz plik:

`:write<Enter>`

- Wyjdź bez zapisywania:

`:quit!<Enter>`

- Otwórz plik pod określonym numerem wiersza:

`vim +{{line_number}} {{path/to/file}}`

- Cofnij ostatnią operację:

`u`

- Wyszukaj wzorzec w pliku (naciśnij `n`/`N` przejść do następnego/poprzedniego dopasowania):

`/{{search_pattern}}<Enter>`

- Wykonaj podstawienie wyrażenia regularnego w całym pliku:

`:%s/{{pattern}}/{{replacement}}/g<Enter>`
