# dnf

> Utilitar de gestionare a pachetelor pentru RHEL, Fedora și CentOS (înlocuiește yum).
> Mai multe informaţii: <https://dnf.readthedocs.io/>

- Upgrade-ul pachetelor instalate la cele mai noi versiuni disponibile:

`sudo dnf upgrade`

- Caută pachete prin cuvinte cheie:

`dnf search {{keywords}}`

- Afișează detalii despre un pachet:

`dnf info {{package}}`

- Instalați un pachet nou:

`sudo dnf install {{package}}`

- Instalați un nou pachet și să își asume da la toate întrebările:

`sudo dnf -y install {{package}}`

- Elimină un pachet:

`sudo dnf remove {{package}}`

- Lista pachetelor instalate:

`dnf list --installed`

- Găsiți ce pachete furnizează un fișier dat:

`dnf provides {{file}}`
