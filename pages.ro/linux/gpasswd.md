# gpasswd

> Administrați `/etc/grup` și `/etc/gshadow`.
> Mai multe informaţii: <https://manned.org/gpasswd>

- Definirea administratorilor grupului:

`sudo gpasswd -A {{user1,user2}} {{group}}`

- Setați lista membrilor grupului:

`sudo gpasswd -M {{user1,user2}} {{group}}`

- Creați o parolă pentru grupul denumit:

`gpasswd {{group}}`

- Adăugați un utilizator la grupul denumit:

`gpasswd -a {{user}} {{group}}`

- Eliminați un utilizator din grupul denumit:

`gpasswd -d {{user}} {{group}}`
