# molecule

> A Molecule segít az Ansible szerepek tesztelésében. További információ: <https://molecule.readthedocs.io>.

- Hozzon létre egy új Ansible-szerepet:

`molecule init role --role-name {{role_name}}`

- Tesztek futtatása:

`molecule test`

- Indítsa el a példányt:

`molecule create`

- A példány konfigurálása:

`molecule converge`

- Jelentkezzen be a példányba:

`molecule login`
