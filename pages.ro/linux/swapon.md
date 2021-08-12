# swapon

> Activează dispozitivul sau fișierul pentru înlocuire.

- Obțineți informații despre swap:

`swapon -s`

- Activați o anumită partiție swap:

`swapon {{/dev/sdb7}}`

- Activați un anumit fișier swap:

`swapon {{path/to/file}}`

- Activează toate zonele swap:

`swapon -a`

- Activați swap prin eticheta unui dispozitiv sau fișier:

`swapon -L {{swap1}}`
