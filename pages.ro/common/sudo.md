# sudo

> Execută o singură comandă ca superuser sau alt utilizator.
> Mai multe informaţii: <https://www.sudo.ws/sudo.html>

- Rulați o comandă ca superuser:

`sudo {{less /var/log/syslog}}`

- Editați un fișier ca superuser cu editorul implicit:

`sudo --edit {{/etc/fstab}}`

- Rulați o comandă ca un alt utilizator și/sau grup:

`sudo --user={{user}} --group={{group}} {{id -a}}`

- Repetați ultima comandă prefixată cu `sudo` (numai în `bash`, `zsh`, etc.):

`sudo !!`

- Lansați shell-ul implicit cu privilegii de superuser și executați fișiere specifice login-specific (`.profile`, `.bash_profile`, etc.):

`sudo --login`

- Lansați shell-ul implicit cu privilegii superuser fără a schimba mediul:

`sudo --shell`

- Lansarea shell-ului implicit ca utilizator specificat, încărcarea mediului utilizatorului și citirea fișierelor specifice login-ului (`.profile`, `.bash_profile`, etc.):

`sudo --login --user={{user}}`

- Listează comenzile permise (și interzise) pentru utilizatorul invocat:

`sudo --list`
