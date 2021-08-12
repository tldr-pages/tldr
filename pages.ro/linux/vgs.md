# vgs

> Afișați informații despre grupurile de volum.
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/vgs.8.html>

- Afișați informații despre grupurile de volum:

`vgs`

- Afișează toate grupurile de volum:

`vgs -a`

- Modificați afișajul implicit pentru a afișa mai multe detalii:

`vgs -v`

- Afișează numai câmpuri specifice:

`vgs -o {{field_name_1}},{{field_name_2}}`

- Adaugă câmp la afișarea implicită:

`vgs -o +{{field_name}}`

- Suprimă linia de titlu:

`vgs --noheadings`

- Utilizați separator pentru a separa câmpurile:

`vgs --separator =`
