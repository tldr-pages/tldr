# git add

> Dodaj zmienione pliki do indeksu.
> Więcej informacji: <https://git-scm.com/docs/git-add>.

- Dodaj plik do indeksu:

`git add {{ścieżka/do/pliku}}`

- Dodaj wszystkie pliki (śledzone i nieśledzone):

`git add {{[-A|--all]}}`

- Dodaj wszystkie pliki w bieżącym katalogu:

`git add .`

- Dodaj tylko już śledzone pliki:

`git add {{[-u|--update]}}`

- Dodaj również ignorowane pliki:

`git add {{[-f|--force]}}`

- Dodawaj części plików interaktywnie:

`git add {{[-p|--patch]}}`

- Dodawaj części określonego pliku interaktywnie:

`git add {{[-p|--patch]}} {{ścieżka/do/pliku}}`

- Dodaj plik interaktywnie:

`git add {{[-i|--interactive]}}`
