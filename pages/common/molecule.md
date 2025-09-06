# molecule

> Molecule helps testing Ansible roles.
> More information: <https://molecule.readthedocs.io>.

- Create a new Ansible role:

`molecule init role --role-name {{role_name}}`

- Run tests:

`molecule test`

- Start the instance:

`molecule create`

- Configure the instance:

`molecule converge`

- List scenarios of the instance:

`molecule matrix converge`

- Log in into the instance:

`molecule login`
