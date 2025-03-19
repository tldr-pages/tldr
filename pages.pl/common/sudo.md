# sudo

> Wykonuje pojedyncze polecenie jako superuser lub inny użytkownik.
> Więcej informacji: <https://www.sudo.ws/sudo.html>.

- Uruchom polecenie jako superuser:

`sudo {{less /var/log/syslog}}`

- Edytuj plik jako superuser w domyślnym edytorze:

`sudo {{[-e|--edit]}} {{/etc/fstab}}`

- Uruchom polecenie jako inny użytkownik i/lub grupa:

`sudo {{[-u|--user]}} {{uzytkownik}} {{[-g|--group]}} {{grupa}} {{id -a}}`

- Powtórz ostatnie polecenie poprzedzone `sudo` (tylko w Bash, Zsh, etc.):

`sudo !!`

- Uruchom domyślną powłokę z uprawnieniami superuser:

`sudo {{[-i|--login]}}`
