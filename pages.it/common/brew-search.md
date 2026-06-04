# brew search

> Cerca cask e formule.
> Maggiori informazioni: <https://docs.brew.sh/Manpage#search--s-options-textregex->.

- Cerca cask e formule usando una parola chiave:

`brew search {{keyword}}`

- Cerca cask e formule usando una `regex`:

`brew search /{{regex}}/`

- Abilita la ricerca nelle descrizioni:

`brew search --desc {{keyword}}`

- Cerca solo le formule:

`brew search --formula {{keyword}}`

- Cerca solo i cask:

`brew search --cask {{keyword}}`
