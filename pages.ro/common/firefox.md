# firefox

> Un browser web gratuit și cu sursă deschisă.
> Mai multe informaţii: <https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options>

- Lansați Firefox și deschideți o pagină web:

`firefox {{https://www.duckduckgo.com}}`

- Deschide o fereastră nouă:

`firefox --new-window {{https://www.duckduckgo.com}}`

- Deschideți o fereastră privată (incognito):

`firefox --private-window`

- Căutați „wikipedia” utilizând motorul de căutare implicit:

`firefox --search "{{wikipedia}}"`

- Lansați Firefox în modul sigur, cu toate extensiile dezactivate:

`firefox --safe-mode`

- Faceți o captură de ecran a unei pagini web în modul fără cap:

`firefox --headless --screenshot {{path/to/output_file.png}} {{https://example.com/}}`

- Folosește un profil specific pentru a permite mai multe instanțe separate ale Firefox să ruleze simultan:

`firefox --profile {{path/to/directory}} {{https://example.com/}}`

- Setați Firefox ca browser implicit:

`firefox --setDefaultBrowser`
