# ansible-գույքագրում

> Ցուցադրել կամ թափել Ansible-ի գույքագրումը:.
> Տես նաև՝ `ansible`:.
> Լրացուցիչ տեղեկություններ. <https://docs.ansible.com/projects/ansible/latest/cli/ansible-inventory.html>:.

- Ցուցադրել լռելյայն գույքագրումը.:

`ansible-inventory --list`

- Ցուցադրել մաքսային գույքագրում.:

`ansible-inventory --list {{[-i|--inventory-file]}} {{path/to/file_or_script_or_directory}}`

- Ցուցադրել լռելյայն գույքագրումը YAML-ում.:

`ansible-inventory --list {{[-y|--yaml]}}`

- Լռել նախնական գույքագրումը ֆայլի մեջ.:

`ansible-inventory --list --output {{path/to/file}}`
