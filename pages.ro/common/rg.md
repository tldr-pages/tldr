# rg

> Ripgrep este un instrument de căutare CLI orientat spre linie recursivă.
> Scopul este de a fi o alternativă mai rapidă la `grep`.
> Mai multe informaţii: <https://github.com/BurntSushi/ripgrep>

- Caută recursiv directorul curent pentru o expresie regulată:

`rg {{regular_expression}}`

- Căutați expresii regulate recursiv în directorul curent, inclusiv fișierele ascunse și fișierele listate în `.gitignore`:

`rg --no-ignore --hidden {{regular_expression}}`

- Căutați o expresie regulată numai într-un anumit tip de fișier (de exemplu, html, css etc.):

`rg --type {{filetype}} {{regular_expression}}`

- Căutați o expresie regulată numai într-un subset de directoare:

`rg {{regular_expression}} {{set_of_subdirs}}`

- Căutați o expresie regulată în fișiere care se potrivesc unui glob (de exemplu, `README.*`):

`rg {{regular_expression}} --glob {{glob}}`

- Doar lista de fișiere potrivite (utile atunci când conducte la alte comenzi):

`rg --files-with-matches {{regular_expression}}`

- Afișați linii care nu se potrivesc cu expresia regulată dată:

`rg --invert-match {{regular_expression}}`

- Caută un model de șir literal:

`rg --fixed-strings -- {{string}}`
