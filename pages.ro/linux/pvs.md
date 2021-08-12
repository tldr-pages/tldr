# pvs

> Afișați informații despre volumele fizice.
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/pvs.8.html>

- Afișează informații despre volumele fizice:

`pvs`

- Afișează volume non-fizice:

`pvs -a`

- Modificați afișajul implicit pentru a afișa mai multe detalii:

`pvs -v`

- Afișează numai câmpuri specifice:

`pvs -o {{field_name_1}},{{field_name_2}}`

- Adaugă câmp la afișarea implicită:

`pvs -o +{{field_name}}`

- Suprimă linia de titlu:

`pvs --noheadings`

- Utilizați separator pentru a separa câmpurile:

`pvs --separator {{special_character}}`
