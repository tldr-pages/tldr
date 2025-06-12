# sudo

> Parancsot futtat superuser vagy más felhasználók nevében.
> További információk: <https://www.sudo.ws/sudo.html>.

- Parancs futtatása superuserként:

`sudo {{less /var/log/syslog}}`

- Fájl szerkesztése a szövegszerkesztő programoddal, superuser jogokkal:

`sudo {{[-e|--edit]}} {{/etc/fstab}}`

- Parancs futtatása más felhasználó és/vagy csoport nevében:

`sudo {{[-u|--user]}} {{user}} {{[-g|--group]}} {{group}} {{id -a}}`

- Előző parancs futtatása `sudo`-val (csakis Bash, Zsh, stb.):

`sudo !!`

- Alap shell futtatása superuser jogokkal és bejelentkezéshez kötött fájlokkal (`.profile`, `.bash_profile`, stb.):

`sudo {{[-i|--login]}}`

- Alap shell futtatása superuser jogokkal, környezet változatása nélkül:

`sudo {{[-s|--shell]}}`

- Alap shell futtatása bizonyos felhasználó nevében, környezetét betöltve és bejelentkezéshez kötött fájlokat beolvasva (`.profile`, `.bash_profile`, stb.):

`sudo {{[-i|--login]}} {{[-u|--user]}} {{user}}`

- Parancsot futtató felhasználó számára tiltott parancsok mutatása:

`sudo {{[-ll|--list --list]}}`
