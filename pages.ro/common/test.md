# test

> Evaluați starea.
> Returnează 0 dacă condiția se evaluează la true, 1 dacă se evaluează la fals.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/test>

- Testați dacă o variabilă dată este egală cu un șir dat:

`test "{{$MY_VAR}}" == "{{/bin/zsh}}"`

- Testați dacă o variabilă dată este goală:

`test -z "{{$GIT_BRANCH}}"`

- Testați dacă există un fișier:

`test -f "{{path/to/file_or_directory}}"`

- Testați dacă un director nu există:

`test ! -d "{{path/to/directory}}"`

- Declaraţie dacă altceva:

`test {{condition}} && {{echo "true"}} || {{echo "false"}}`
