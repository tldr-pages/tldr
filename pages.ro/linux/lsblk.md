# lsblk

> Listează informații despre dispozitive.

- Listează toate dispozitivele de stocare într-un format de copac:

`lsblk`

- De asemenea, lista de dispozitive goale:

`lsblk -a`

- Imprimați coloana SIZE în octeți, mai degrabă decât într-un format care poate fi citit de om:

`lsblk -b`

- Informații de ieșire despre sistemele de fișiere:

`lsblk -f`

- Utilizați caractere ASCII pentru formatarea arborelui:

`lsblk -i`

- Informații de ieșire despre topologia bloc-dispozitiv:

`lsblk -t`

- Excludeți dispozitivele specificate de lista separată prin virgulă a numerelor majore de dispozitive:

`lsblk -e {{1,7}}`

- Afișați un rezumat personalizat utilizând o listă de coloane separate prin virgulă:

`lsblk --output {{NAME}},{{SERIAL}},{{MODEL}},{{TRAN}},{{TYPE}},{{SIZE}},{{FSTYPE}},{{MOUNTPOINT}}`
