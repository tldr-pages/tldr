# ansible

> Gestionați grupuri de computere de la distanță prin SSH.
> Utilizați fișierul `/etc/ansible/hosts` pentru a adăuga noi grupuri/gazde.
> Mai multe informaţii: <https://www.ansible.com/>

- Lista gazdelor aparținând unui grup:

`ansible {{group}} --list-hosts`

- Ping un grup de gazde prin invocarea modulului ping:

`ansible {{group}} -m ping`

- Afișați fapte despre un grup de gazde prin invocarea modulului de configurare:

`ansible {{group}} -m setup`

- Executa o comanda pe un grup de gazde prin invocarea modulului de comanda cu argumente:

`ansible {{group}} -m command -a '{{my_command}}'`

- Execută o comandă cu privilegii administrative:

`ansible {{group}} --become --ask-become-pass -m command -a '{{my_command}}'`

- Executați o comandă utilizând un fișier de inventar personalizat:

`ansible {{group}} -i {{inventory_file}} -m command -a '{{my_command}}'`

- Listează grupurile într-un inventar:

`ansible localhost -m debug -a '{{var=groups.keys()}}'`
