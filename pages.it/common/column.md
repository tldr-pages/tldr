# column

> Formatta standard input o un file in più colonne.
> Le colonne sono riempite prima delle righe; il separatore predefinito è lo spazio.
> Maggiori informazioni: <https://manned.org/column>.

- Formatta l'output per uno schermo largo 30 caratteri:

`printf "intestazione1 intestazione2\nbar foo\n" | column --output-width {{30}}`

- Separa colonne ed allinea automaticamente in un formato tabulare:

`printf "intestazione1 intestazione2\nbar foo\n" | column --table`

- Specifica un diverso separatore di colonna (e.g. "," per CSV) (il predefinito è lo spazio):

`printf "intestazione1 intestazione2\nbar foo\n" | column --table --separator {{,}}`

- Riempi le righe prima delle colonne:

`printf "intestazione1\nbar\nfoobar\n" | column --output-width {{30}} --fillrows`
