# lvs

> Afișați informații despre volumele logice.
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/lvs.8.html>

- Afișați informații despre volumele logice:

`lvs`

- Afișează toate volumele logice:

`lvs -a`

- Modificați afișajul implicit pentru a afișa mai multe detalii:

`lvs -v`

- Afișează numai câmpuri specifice:

`lvs -o {{field_name_1}},{{field_name_2}}`

- Adaugă câmp la afișarea implicită:

`lvs -o +{{field_name}}`

- Suprimă linia de titlu:

`lvs --noheadings`

- Utilizați un separator pentru a separa câmpurile:

`lvs --separator {{=}}`
