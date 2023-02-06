# makepasswd

> Jelszavak generálása és titkosítása. További információ: <https://manpages.debian.org/stretch/makepasswd/makepasswd.1.en.html>.

- Generáljon véletlenszerű jelszót (8-10 karakter hosszú, betűket és számokat tartalmazó):

`makepasswd`

- Generáljon egy 10 karakter hosszú jelszót:

`makepasswd --chars {{10}}`

- 5-10 karakter hosszú jelszó generálása:

`makepasswd --minchars {{5}} --maxchars {{10}}`

- Csak a "b", "a" vagy "r" karaktereket tartalmazó jelszó generálása:

`makepasswd --string {{bar}}`
