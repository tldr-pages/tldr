# swapoff

> Dezactivează dispozitivul sau fișierul pentru înlocuire.

- Dezactivați o anumită partiție swap:

`swapoff {{/dev/sdb7}}`

- Dezactivați un fișier swap dat:

`swapoff {{path/to/file}}`

- Dezactivați toate zonele swap:

`swapoff -a`

- Dezactivați swap prin eticheta unui dispozitiv sau fișier:

`swapoff -L {{swap1}}`
