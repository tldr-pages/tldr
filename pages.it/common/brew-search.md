# brew search

> Cerca cask e formule.
> Maggiori informazioni: <https://docs.brew.sh/Manpage#search--s-options-textregex->.

- Cerca cask e formule usando una parola chiave:

`brew search {{parola_chiave}}`

- Cerca cask e formule usando una `regex`:

`brew search /{{regex}}/`

- Abilita la ricerca nelle descrizioni:

`brew search --desc {{parola_chiave}}`

- Cerca solo le formule:

`brew search --formula {{parola_chiave}}`

- Cerca solo i cask:

`brew search --cask {{parola_chiave}}`
