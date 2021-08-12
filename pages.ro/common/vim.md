# vim

> Vim (Vi Îmbunătățit), un editor de text în linia de comandă, oferă mai multe moduri pentru diferite tipuri de manipulare a textului.
> Apăsând `i `intră în modul inserare. `<Esc>` intră în modul normal, care permite utilizarea comenzilor Vim.
> Mai multe informaţii: <https://www.vim.org>

- Deschide un fișier:

`vim {{path/to/file}}`

- Vezi manualul de ajutor al lui Vim:

`:help<Enter>`

- Salvează şi renunţă:

`:wq<Enter>`

- Deschideți un fișier la un număr de linie specificat:

`vim +{{line_number}} {{path/to/file}}`

- Anulează ultima operație:

`u`

- Căutați un model în fișier (apăsați `n`/`n` pentru a merge la meciul următor/anterior):

`/{{search_pattern}}<Enter>`

- Efectuați o substituție de expresie regulată în întregul fișier:

`:%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- Afișează numerele de linie:

`:set nu<Enter>`
