# exa

> Un moderno sostituto per `ls` (elenca i contenuti di una directory).
> Maggiori informazioni: <https://github.com/ogham/exa#command-line-options>.

- Elenca i file nella directory corrente, uno per riga:

`exa {{[-1|--oneline]}}`

- Elenca tutti i file, inclusi quelli nascosti:

`exa {{[-a|--all]}}`

- Elenca tutti i file e mostra informazioni (permessi, dimensione e data di ultima modifica):

`exa {{[-l|--long]}} {{[-a|--all]}}`

- Elenca i file, ordinandoli per dimensione decrescente:

`exa {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Mostra un albero dei file con 3 livelli di profondità:

`exa {{[-l|--long]}} {{[-T|--tree]}} {{[-L|--level]}} {{3}}`

- Elenca i file e mostra informazioni, ordinandoli per ultima modifica (più vechci prima):

`exa {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`
