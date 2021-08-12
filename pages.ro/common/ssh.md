# ssh

> Secure Shell este un protocol folosit pentru a vă conecta în siguranță la sistemele de la distanță.
> Poate fi folosit pentru înregistrarea în jurnal sau executarea comenzilor pe un server la distanță.

- Conectează-te la un server de la distanță:

`ssh {{username}}@{{remote_host}}`

- Conectați-vă la un server de la distanță cu o anumită identitate (cheie privată):

`ssh -i {{path/to/key_file}} {{username}}@{{remote_host}}`

- Conectați-vă la un server de la distanță utilizând un anumit port:

`ssh {{username}}@{{remote_host}} -p {{2222}}`

- Rulați o comandă pe un server la distanță:

`ssh {{remote_host}} {{command -with -flags}}`

- Tunelare SSH: Redirecționare dinamică a portului (SOCKS proxy pe localhost:1080):

`ssh -D {{1080}} {{username}}@{{remote_host}}`

- Tunelare SSH: Redirecționați un anumit port (localhost:9999 la exemplu.org:80) împreună cu dezactivarea alocării pseudo- [t] ty și execuutio [n] de comenzi la distanță:

`ssh -L {{9999}}:{{example.org}}:{{80}} -N -T {{username}}@{{remote_host}}`

- SSH jumping: Conectați-vă printr-un jumphost la un server de la distanță (Mai multe salturi pot fi specificate separate prin caractere virgulă):

`ssh -J {{username}}@{{jump_host}} {{username}}@{{remote_host}}`

- Redirecționarea agentului: Redirecționați informațiile de autentificare către mașina de la distanță (consultați `man ssh_config` pentru opțiunile disponibile):

`ssh -A {{username}}@{{remote_host}}`
