# ansible-inventory

> Afișați sau aruncați un inventar Ansible.
> A se vedea, de asemenea,: „ansible”.
> Mai multe informaţii: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>

- Afișează inventarul implicit:

`ansible-inventory --list`

- Afișează un inventar personalizat:

`ansbile-inventory --list --inventory {{path/to/file_or_script_or_directory}}`

- Afișează inventarul implicit în YAML:

`ansible-inventory --list --yaml`

- Dump inventarul implicit într-un fișier:

`ansible-inventory --list --output {{path/to/file}}`
