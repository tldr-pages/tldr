# stty

> Setaţi opţiunile pentru o interfaţă a dispozitivului terminal.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/stty>

- Afișează toate setările pentru terminalul curent:

`stty -a`

- Setați numărul de rânduri:

`stty rows {{rows}}`

- Setați numărul de coloane:

`stty cols {{cols}}`

- Obțineți viteza reală de transfer a unui dispozitiv:

`stty -F {{path/to/device_file}} speed`

- Resetați toate modurile la valori rezonabile pentru terminalul curent:

`stty sane`
