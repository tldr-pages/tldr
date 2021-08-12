# molecule

> Molecula ajută la testarea rolurilor ansibile.
> Mai multe informaţii: <https://molecule.readthedocs.io>

- Crearea unui nou rol ansible:

`molecule init role --role-name {{role_name}}`

- Executaţi teste:

`molecule test`

- Porniţi instanţa:

`molecule create`

- Configurați instanța:

`molecule converge`

- Autentificaţi-vă în instanţă:

`molecule login`
