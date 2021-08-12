# sha512sum

> Calculați sumele de verificare criptografice SHA512.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>

- Calculați suma de control SHA512 pentru un fișier:

`sha512sum {{filename1}}`

- Calculați sumele de control SHA512 pentru mai multe fișiere:

`sha512sum {{filename1}} {{filename2}}`

- Calculați și salvați lista sumelor de control SHA512 într-un fișier:

`sha512sum {{filename1}} {{filename2}} > {{filename.sha512}}`

- Citiți un fișier de sume SHA512 și verificați toate fișierele au sumuri de control potrivite:

`sha512sum --check {{filename.sha512}}`

- Afișați doar un mesaj pentru fișierele pentru care verificarea nu reușește:

`sha512sum --check --quiet {{filename.sha512}}`
