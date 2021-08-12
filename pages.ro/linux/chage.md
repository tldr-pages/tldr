# chage

> Modificați informațiile privind expirarea contului de utilizator și a parolei.
> Mai multe informaţii: <https://manned.org/chage>

- Lista informațiilor despre parolă pentru utilizator:

`chage -l {{username}}`

- Activați expirarea parolei în 10 zile:

`sudo chage -M {{10}} {{username}}`

- Dezactivează expirarea parolei:

`sudo chage -M -1 {{username}}`

- Setați data expirării contului:

`sudo chage -E {{YYYY-MM-DD}}`

- Forțați utilizatorul să schimbe parola la următoarea conectare:

`sudo chage -d 0`
