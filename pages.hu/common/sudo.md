# sudo

> Egyetlen parancsot hajt végre szuperfelhasználóként vagy más felhasználóként. További információ: <https://www.sudo.ws/sudo.html>.

- Parancs futtatása superuser-ként:

`sudo {{less /var/log/syslog}}`

- Egy fájl szerkesztése superuser-ként az alapértelmezett szerkesztővel:

`sudo --edit {{/etc/fstab}}`

- Egy parancs futtatása más felhasználóként és/vagy csoportként:

`sudo --user={{user}} --group={{group}} {{id -a}}`

- Az utolsó, `sudo` előtaggal ellátott parancs megismétlése (csak a `bash`, `zsh`, stb. esetén):

`sudo !!`

- Indítsa el az alapértelmezett héjat szuperfelhasználói jogosultságokkal, és futtassa a bejelentkezésre vonatkozó fájlokat (`.profile`, `.bash_profile`, stb.):

`sudo --login`

- Indítsa el az alapértelmezett héjat superuser jogosultságokkal a környezet megváltoztatása nélkül:

`sudo --shell`

- Az alapértelmezett héj elindítása a megadott felhasználóként, a felhasználói környezet betöltésével és a bejelentkezés-specifikus fájlok beolvasásával (`.profile`, `.bash_profile`, stb.):

`sudo --login --user={{user}}`

- A meghívó felhasználó számára engedélyezett (és tiltott) parancsok listázása:

`sudo --list`
