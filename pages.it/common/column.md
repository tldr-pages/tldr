# column

> Formatta standard input o un file in più colonne.
> Le righe sono riempite prima delle colonne; il separatore predefinito è lo spazio.

- Formatta l'output per uno schermo largo 30 caratteri:

`printf "intestazione1 intestazione2\nbar foo\n" | column -c {{30}}`

- Specifica un diverso separatore di colonna (e.g. "," per csv); il predefinito è lo spazio:

`printf "intestazione1 intestazione2\nbar foo\n" | column -s{{,}}`

- Separa colonne ed allinea automaticamente in un formato tabulare:

`printf "intestazione1 intestazione2\nbar foo\n" | column -t`

- Riempi le colonne prima delle righe:

`printf "intestazione1\nbar\nfoobar\n" | column -c {{30}} -x`
