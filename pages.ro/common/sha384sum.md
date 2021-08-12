# sha384sum

> Calculați sumele de verificare criptografice SHA384.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>

- Calculați suma de control SHA384 pentru un fișier:

`sha384sum {{filename1}}`

- Calculați sumele de control SHA384 pentru mai multe fișiere:

`sha384sum {{filename1}} {{filename2}}`

- Calculați și salvați lista sumelor de control SHA384 într-un fișier:

`sha384sum {{filename1}} {{filename2}} > {{filename.sha384}}`

- Citiți un fișier cu sume SHA384 și verificați că toate fișierele au sume de control potrivite:

`sha384sum --check {{filename.sha384}}`

- Afișați doar un mesaj pentru fișierele pentru care verificarea nu reușește:

`sha384sum --check --quiet {{filename.sha384}}`
