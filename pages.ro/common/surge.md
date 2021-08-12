# surge

> Publicare web simplă în linia de comandă.
> Mai multe informaţii: <https://surge.sh>

- Încărcați un site nou la surge.sh:

`surge {{path/to/my_project}}`

- Implementați site-ul la domeniu particularizat (rețineți că înregistrările DNS trebuie să indice subdomeniul surge.sh):

`surge {{path/to/my_project}} {{my_custom_domain.com}}`

- Listează proiectele tale de supratensiune:

`surge list`

- Elimină un proiect:

`surge teardown {{my_custom_domain.com}}`
