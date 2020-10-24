# molecule

> Molecule helps testing ansible roles.
> More information: <https://molecule.readthedocs.io>.

- Create a new ansible role:

`molecule init role --role-name {{role_name}}`

- Run tests:

`molecule test`

- Start the instance:

`molecule create`

- Configure the instance:

`molecule converge`

- Login into the instance:

`molecule login`
