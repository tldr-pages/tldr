# exa

> Un moderno sostituto per `ls` (elenca i contenuti di una cartella).
> Maggiori informazioni: <https://the.exa.website>.

- Elenca i file nella cartella corrente, uno per riga:

`exa --oneline`

- Elenca tutti i file, inclusi quelli nascosti:

`exa --all`

- Elenca tutti i file e mostra informazioni (permessi, dimensione e data di ultima modifica):

`exa --long --all`

- Elenca i file, ordinandoli per dimensione decrescente:

`exa --reverse --sort={{size}}`

- Mostra un albero dei file con 3 livelli di profondità:

`exa --long --tree --level={{3}}`

- Elenca i file e mostra informazioni, ordinandoli per ultima modifica (più vechci prima):

`exa --long --sort={{modified}}`
