# exa

> Un înlocuitor modern pentru `ls` (conținutul directorului listei).
> Mai multe informaţii: <https://the.exa.website>

- Lista fişierelor una pe linie:

`exa --oneline`

- Listați toate fișierele, inclusiv fișierele ascunse:

`exa --all`

- Lista de format lung (permisiuni, proprietate, dimensiune și data modificării) a tuturor fișierelor:

`exa --long --all`

- Lista fișierelor cu cea mai mare în partea de sus:

`exa --reverse --sort={{size}}`

- Afișează un copac de fișiere, trei niveluri adâncime:

`exa --long --tree --level={{3}}`

- Lista fișierelor sortate după data modificării (prima cea mai veche):

`exa --long --sort={{modified}}`

- Listează fișierele cu anteturile, pictogramele și stările Git:

`exa --long --header --icons --git`

- Nu listați fișierele menționate în `.gitignore`:

`exa --git-ignore`
