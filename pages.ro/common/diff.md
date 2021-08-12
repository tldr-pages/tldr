# diff

> Comparați fișierele și directoarele.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man1/diff.1.html>

- Comparați fișierele (listează modificările pentru a transforma `old_file` în `new_file`):

`diff {{old_file}} {{new_file}}`

- Comparați fișierele, ignorând spațiile albe:

`diff -w {{old_file}} {{new_file}}`

- Comparați fișierele, arătând diferențele una lângă alta:

`diff -y {{old_file}} {{new_file}}`

- Comparați fișierele, arătând diferențele în format unificat (așa cum este utilizat de `git dif`):

`diff -u {{old_file}} {{new_file}}`

- Comparați directoarele recursiv (afișează numele pentru diferite fișiere/directoare, precum și modificările aduse fișierelor):

`diff -r {{old_directory}} {{new_directory}}`

- Comparați directoarele, afișând numai numele fișierelor care diferă:

`diff -rq {{old_directory}} {{new_directory}}`
