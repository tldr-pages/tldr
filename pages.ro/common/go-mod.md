# go mod

> Întreținerea modulului.
> Mai multe informaţii: <https://golang.org/cmd/go/#hdr-Module_maintenance>

- Inițializarea modulului nou în directorul curent:

`go mod init {{moduleName}}`

- Descărcați module în memoria cache locală:

`go mod download`

- Adăugați lipsă și eliminați modulele neutilizate:

`go mod tidy`

- Verificați că dependențele au conținut așteptat:

`go mod verify`

- Copiați sursele tuturor dependențelor în directorul vânzătorului:

`go mod vendor`
