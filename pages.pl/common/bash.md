# bash

> Bourne-Again SHell, interpreter komend powłoki systemowej kompatybilny z `sh`.
> Zobacz także: `zsh`, `histexpand`.
> Więcej informacji: <https://www.gnu.org/software/bash/manual/bash.html#Invoking-Bash>.

- Rozpocznij interaktywną sesję powłoki:

`bash`

- Rozpocznij interaktywną sesję powłoki bez ładowania konfiguracji:

`bash --norc`

- Wywołaj określone komendy:

`bash -c "{{echo 'bash jest uruchomiony'}}"`

- Uruchom podany skrypt:

`bash {{ścieżka/do/skryptu.sh}}`

- Wykonaj podany skrypt, wypisując wszystkie komendy przed ich wykonaniem:

`bash -x {{ścieżka/do/skryptu.sh}}`

- Wykonaj podany skrypt do wystąpienia pierwszego błędu:

`bash -e {{ścieżka/do/skryptu.sh}}`

- Wykonaj komendy ze `stdin`:

`{{echo "echo 'bash jest uruchomiony'"}} | bash`

- Uruchom sesję w trybie [r]estrykcyjnym:

`bash -r`
