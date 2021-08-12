# bup

> Sistem de backup bazat pe formatul Git packfile, oferind salvări incrementale și eliminare globală a duplicatelor.
> Mai multe informaţii: <https://github.com/bup/bup>

- Inițializați un depozit de rezervă în directorul local specificat:

`bup -d {{path/to/repository}} init`

- Pregătiți un director dat înainte de a lua o copie de rezervă:

`bup -d {{path/to/repository}} index {{path/to/directory}}`

- Copierea de rezervă a unui director în depozit:

`bup -d {{path/to/repository}} save -n {{backup_name}} {{path/to/directory}}`

- Afișați instantaneele de rezervă stocate în prezent în depozit:

`bup -d {{path/to/repository}} ls`

- Restaurați un instantaneu de rezervă specific într-un director țintă:

`bup -d {{path/to/repository}} restore -C {{path/to/target_directory}} {{backup_name}}`
