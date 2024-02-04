# bash

> Bourne-Again SHell, interpreter komend powłoki systemowej kompatybilny z tradycyjnym `sh`.
> Więcej informacji na stronie: <https://www.gnu.org/software/bash/>.

- Rozpocznij interaktywną sesję terminalu Bash:

  `bash`

- Rozpocznij interaktywną sesję terminalu bash bez ładowania startowej konfiguracji:

  `bash --norc`

- `-c` Wywołaj określoną komendę w powłoce Bash:

  `bash -c "{{komenda powłoki systemowej}}"`

- Uruchom przekazany jako argument skrypt shella:

  `bash {{sciezka/do/skrypt.sh}}`

- `-x` Wykonaj przekazany jako argument skrypt, wypisując wszystkie wykonane w procesie komendy na standardowe wyjście `stdout`:

  `bash -x {{sciezka/do/skrypt.sh}}`

- `-e` Wykonaj przekazany skrypt do pojawienia się pierwszego błędu:

  `bash -e {{sciezka/do/skrypt.sh}}`

- Wykonaj komendę przekazaną przez strumień wejścia `stdin`:

  `{{echo "echo 'bash uruchomiony'"}} | bash`

- `-r` Uruchom sesję Bash w trybie [r]estrykcyjnym (więcej o trybie restrykcyjnym na stronie <https://www.gnu.org/software/bash/manual/html_node/The-Restricted-Shell.html>):

  `bash -r`
