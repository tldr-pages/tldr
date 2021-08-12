# echo

> Tipărește argumentele date.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/echo>

- Tipăreşte un mesaj text. Notă: ghilimelele sunt opționale:

`echo "{{Hello World}}"`

- Imprimați un mesaj cu variabile de mediu:

`echo "{{My path is $PATH}}"`

- Imprimați un mesaj fără linia nouă la sfârșit:

`echo -n "{{Hello World}}"`

- Adăugați un mesaj la fișier:

`echo "{{Hello World}}" >> {{file.txt}}`

- Activați interpretarea evadărilor backslash (caractere speciale):

`echo -e "{{Column 1\tColumn 2}}"`
