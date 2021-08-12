# codespell

> Verificator ortografic pentru codul sursă.
> Mai multe informaţii: <https://github.com/codespell-project/codespell>

- Verificați greșelile de ortografie în toate fișierele text din directorul curent, recursiv:

`codespell`

- Corectați toate greșelile de ortografie găsite în loc:

`codespell --write-changes`

- Omite fișiere cu nume care se potrivesc cu modelul specificat (acceptă o listă separată prin virgulă de modele folosind metacaractere):

`codespell --skip "{{pattern}}"`

- Utilizați un fișier de dicționar personalizat atunci când bifați (`—dicționarul' poate fi folosit de mai multe ori):

`codespell --dictionary {{path/to/file.txt}}`

- Nu verificați cuvintele care sunt listate în fișierul specificat:

`codespell --ignore-words {{path/to/file.txt}}`

- Nu verificați cuvintele specificate:

`codespell --ignore-words-list {{words,to,ignore}}`

- Imprimați 3 linii de context în jurul, înainte sau după fiecare meci:

`codespell --{{context|before-context|after-context}} {{3}}`

- Verificați numele fișierelor pentru greșeli de ortografie, în plus față de conținutul fișierului:

`codespell --check-filenames`
