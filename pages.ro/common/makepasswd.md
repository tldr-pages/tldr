# makepasswd

> Generare și criptare parole.
> Mai multe informaţii: <https://manpages.debian.org/stretch/makepasswd/makepasswd.1.en.html>

- Generați o parolă aleatorie (8 până la 10 caractere lungime, conținând litere și numere):

`makepasswd`

- Generează o parolă lungă de 10 caractere:

`makepasswd --chars {{10}}`

- Generează o parolă de 5 până la 10 caractere:

`makepasswd --minchars {{5}} --maxchars {{10}}`

- Generați o parolă care conține doar caracterele „b”, „a” sau „r”:

`makepasswd --string {{bar}}`
