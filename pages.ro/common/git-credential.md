# git credential

> Recuperarea și stocarea acreditărilor de utilizator.
> Mai multe informaţii: <https://git-scm.com/docs/git-credential>

- Afișarea informațiilor de acreditare, preluarea numelui de utilizator și a parolei din fișierele de configurare:

`echo "{{url=http://example.com}}" | git credential fill`

- Trimiteți informații de acreditare tuturor asistenților de acreditare configurați pentru a stoca pentru utilizare ulterioară:

`echo "{{url=http://example.com}}" | git credential approve`

- Ștergeți informațiile de acreditare specificate din toate ajutoarele de acreditare configurate:

`echo "{{url=http://example.com}}" | git credential reject`
