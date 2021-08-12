# git column

> Afișarea datelor în coloane.
> Mai multe informaţii: <https://git-scm.com/docs/git-column>

- Formatați intrarea standard ca mai multe coloane:

`ls | git column --mode={{column}}`

- Formatarea intrării standard ca mai multe coloane cu o lățime maximă de `100”:

`ls | git column --mode=column --width={{100}}`

- Formatarea intrării standard ca mai multe coloane cu o căptușeală maximă de `30`:

`ls | git column --mode=column --padding={{30}}`
