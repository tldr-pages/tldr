# security-checker

> Verificaţi dacă o aplicaţie PHP utilizează dependenţe cu vulnerabilităţi de securitate cunoscute.
> Mai multe informaţii: <https://github.com/sensiolabs/security-checker>

- Căutați probleme de securitate în dependențele proiectului (pe baza fișierului `composer.lock` din directorul curent):

`security-checker security:check`

- Folosește un fișier specific `composer.lock`:

`security-checker security:check {{path/to/composer.lock}}`

- Returnează rezultatele ca obiect JSON:

`security-checker security:check --format=json`
