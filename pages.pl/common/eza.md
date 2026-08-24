# eza

> Nowoczesny odpowiednik `ls`, fork `exa`.
> Więcej informacji: <https://github.com/eza-community/eza>.

- Wyświetl listę plików, po jednym w linii:

`eza {{[-1|--oneline]}}`

- Wyświetl wszystkie pliki, łącznie z ukrytymi:

`eza {{[-a|--all]}}`

- Wyświetl listę wszystkich plików ze szczegółami (uprawnienia, właściciel, wielkość i data zmiany):

`eza {{[-al|--all --long]}}`

- Wyświetl listę plików posortowaną względem wielkości pliku, od największego:

`eza {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Wyświetl drzewko plików (trzy poziomy):

`eza {{[-lT|--long --tree]}} {{[-L|--level]}} {{3}}`

- Wyświetl listę plików posortowaną względem daty zmiany, od najstarszego:

`eza {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- Wyświetl listę plików wraz z nagłówkiem, ikoną i statusem Git:

`eza {{[-lh|--long --header]}} --icons --git`

- Wyświetl listę plików, ignorując pliki z `.gitignore`:

`eza --git-ignore`
