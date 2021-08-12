# xargs

> Execută o comandă cu argumente tubulare provenind de la o altă comandă, un fișier etc.
> Intrarea este tratată ca un singur bloc de text și împărțită în bucăți separate pe spații, file, linii noi și sfârșitul fișierului.

- Rulați o comandă folosind datele de intrare ca argumente:

`{{arguments_source}} | xargs {{command}}`

- Rulați mai multe comenzi înlănțuite pe datele de intrare:

`{{arguments_source}} | xargs sh -c "{{command1}} && {{command2}} | {{command3}}"`

- Ștergeți toate fișierele cu o extensie `.backup` (`-print0` folosește un caracter nul pentru a împărți numele fișierelor, iar `-0` îl folosește ca delimitator):

`find . -name {{'*.backup'}} -print0 | xargs -0 rm -v`

- Executați comanda o dată pentru fiecare linie de intrare, înlocuind orice apariție a substituentului (aici marcat ca `_`) cu linia de intrare:

`{{arguments_source}} | xargs -I _ {{command}} _ {{optional_extra_arguments}}`

- Se execută paralele ale proceselor de până la `max-procs` la un moment dat; valoarea implicită este 1. Dacă `max-procs` este 0, xargs va rula cât mai multe procese posibil la un moment dat:

`{{arguments_source}} | xargs -P {{max-procs}} {{command}}`
