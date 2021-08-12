# update-alternatives

> Un instrument convenabil pentru menținerea legăturilor simbolice pentru a determina comenzile implicite.
> Mai multe informaţii: <https://manned.org/update-alternatives>

- Adăugați o legătură simbolică:

`sudo update-alternatives --install {{path/to/symlink}} {{command_name}} {{path/to/command_binary}} {{priority}}`

- Configurați o legătură simbolică pentru `java`:

`sudo update-alternatives --config {{java}}`

- Eliminați o legătură simbolică:

`sudo update-alternatives --remove {{java}} {{/opt/java/jdk1.8.0_102/bin/java}}`

- Afișați informații despre o comandă specificată:

`update-alternatives --display {{java}}`

- Afișează toate comenzile și selecția lor curentă:

`update-alternatives --get-selections`
