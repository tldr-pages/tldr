# timeshift

> Utilitar de restaurare sistem.
> Mai multe informaţii: <https://github.com/teejee2008/timeshift>

- Listează instantanee:

`sudo timeshift --list`

- Creați un nou instantaneu (dacă este programat):

`sudo timeshift --check`

- Creați un nou instantaneu (chiar dacă nu este programat):

`sudo timeshift --create`

- Restaurați un instantaneu (selectând ce instantaneu să restaurați interactiv):

`sudo timeshift --restore`

- Restaurați un anumit instantaneu:

`sudo timeshift --restore --snapshot '{{snapshot}}'`

- Ștergeți un anumit instantaneu:

`sudo timeshift --delete --snapshot '{{snapshot}}'`
