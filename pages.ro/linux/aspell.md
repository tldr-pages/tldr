# aspell

> Verificator ortografic interactiv.
> Mai multe informaţii: <http://aspell.net/>

- Verificarea ortografică a unui singur fișier:

`aspell check {{path/to/file}}`

- Lista cuvintelor ortografiate greșit din intrarea standard:

`cat {{file}} | aspell list`

- Afișează limbile dicționarului disponibile:

`aspell dicts`

- Run aspell cu diferite limbi (ia două litere ISO 639 cod de limbă):

`aspell --lang={{cs}}`

- Listați cuvintele greșite din introducerea standard și ignorați cuvintele din lista personală de cuvinte:

`cat {{file}} | aspell --personal={{personal-word-list.pws}} {{list}}`
