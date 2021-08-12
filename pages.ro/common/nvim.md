# nvim

> Neovim, editorul de text al unui programator bazat pe Vim, oferă mai multe moduri pentru diferite tipuri de manipulare a textului.
> Apăsând `i `intră în modul de editare. <Esc>` revine la modul normal, ceea ce nu permite inserarea regulată a textului.
> Mai multe informaţii: <https://neovim.io>

- Deschide un fișier:

`nvim {{file}}`

- Introduceți modul de editare a textului (modul inserare):

`<Esc>i`

- Copiați („smulgeți”) sau tăiați („ștergeți”) linia curentă (lipiți-o cu „P”):

`<Esc>{{yy|dd}}`

- Anulează ultima operație:

`<Esc>u`

- Căutați un model în fișier (apăsați `n`/`n` pentru a merge la meciul următor/anterior):

`<Esc>/{{search_pattern}}<Enter>`

- Efectuați o substituție de expresie regulată în întregul fișier:

`<Esc>:%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- Salvați (scrieți) fișierul și ieșiți:

`<Esc>:wq<Enter>`

- Renunţă fără a salva:

`<Esc>:q!<Enter>`
