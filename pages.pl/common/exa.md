# exa

> Nowoczesny odpowiednik `ls` (wyświetla zawartość katalogu).
> Więcej informacji: <https://github.com/ogham/exa#command-line-options>.

- Wyświetl listę plików, po jednym w linii:

`exa {{[-1|--oneline]}}`

- Wyświetl wszystkie pliki, łącznie z ukrytymi:

`exa {{[-a|--all]}}`

- Wyświetl listę wszystkich plików ze szczegółami (uprawnienia, właściciel, wielkość i data zmiany):

`exa {{[-l|--long]}} {{[-a|--all]}}`

- Wyświetl listę plików posortowaną względem wielkości pliku, od największego:

`exa {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Wyświetl drzewko plików (trzy poziomy):

`exa {{[-l|--long]}} {{[-T|--tree]}} {{[-L|--level]}} {{3}}`

- Wyświetl listę plików posortowaną względem daty zmiany, od najstarszego:

`exa {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- Wyświetl listę plików wraz z nagłówkiem, ikoną i statusem Git:

`exa {{[-l|--long]}} {{[-h|--header]}} --icons --git`

- Wyświetl listę plików, ignorując pliki z `.gitignore`:

`exa --git-ignore`
