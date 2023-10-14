# eza

> Nowoczesny odpowiednik `ls`, fork `exa`.
> Więcej informacji: <https://github.com/eza-community/eza>.

- Wyświetl listę plików, po jednym w linii:

`eza --oneline`

- Wyświetl wszystkie pliki, łącznie z ukrytymi:

`eza --all`

- Wyświetl listę wszystkich plików ze szczegółami (uprawnienia, właściciel, wielkość i data zmiany):

`eza --long --all`

- Wyświetl listę plików posortowaną względem wielkości pliku, od największego:

`eza --reverse --sort={{size}}`

- Wyświetl drzewko plików (trzy poziomy):

`eza --long --tree --level={{3}}`

- Wyświetl listę plików posortowaną względem daty zmiany, od najstarszego:

`eza --long --sort={{modified}}`

- Wyświetl listę plików wraz z nagłówkiem, ikoną i statusem Git:

`eza --long --header --icons --git`

- Wyświetl listę plików, ignorując pliki z `.gitignore`:

`eza --git-ignore`
