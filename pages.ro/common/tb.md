# tb

> CLI pentru gestionarea activităților și notelor în mai multe panouri.
> Mai multe informaţii: <https://github.com/klaussinani/taskbook>

- Adaugă o sarcină nouă la un panou:

`tb --task {{task_description}} @{{board_name}}`

- Adaugă o notă nouă la un panou:

`tb --note {{note_description}} @{{board_name}}`

- Editează prioritatea elementului:

`tb --priority @{{item_id}} {{priority}}`

- Verificare/debifa element:

`tb --check {{item_id}}`

- Arhivează toate elementele verificate:

`tb --clear`

- Mutați elementul pe un panou:

`tb --move @{{item_id}} {{board_name}}`
