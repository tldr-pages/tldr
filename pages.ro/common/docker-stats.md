# docker stats

> Afișează un flux live de statistici privind utilizarea resurselor pentru containere.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/stats/>

- Afișează un flux live pentru statisticile tuturor containerelor care rulează:

`docker stats`

- Afișează un flux live de statistici pentru o listă de containere separate în spațiu:

`docker stats {{container_name}}`

- Modificați formatul coloanelor pentru a afișa procentul de utilizare a procesorului containerului:

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- Afișează statistici pentru toate containerele (ambele rulează și oprit):

`docker stats --all`

- Dezactivați statisticile de streaming și trageți numai statisticile curente:

`docker stats --no-stream`
