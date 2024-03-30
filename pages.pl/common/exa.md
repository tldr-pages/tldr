# exa

> Nowoczesny odpowiednik `ls` (wyświetla zawartość katalogu).
> Więcej informacji: <https://the.exa.website>.

- Wyświetl listę plików, po jednym w linii:

`exa --oneline`

- Wyświetl wszystkie pliki, łącznie z ukrytymi:

`exa --all`

- Wyświetl listę wszystkich plików ze szczegółami (uprawnienia, właściciel, wielkość i data zmiany):

`exa --long --all`

- Wyświetl listę plików posortowaną względem wielkości pliku, od największego:

`exa --reverse --sort={{size}}`

- Wyświetl drzewko plików (trzy poziomy):

`exa --long --tree --level={{3}}`

- Wyświetl listę plików posortowaną względem daty zmiany, od najstarszego:

`exa --long --sort={{modified}}`

- Wyświetl listę plików wraz z nagłówkiem, ikoną i statusem Git:

`exa --long --header --icons --git`

- Wyświetl listę plików, ignorując pliki z `.gitignore`:

`exa --git-ignore`
