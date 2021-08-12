# sha224sum

> Calculați sumele de control criptografice SHA224.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>

- Calculați suma de control SHA224 pentru un fișier:

`sha224sum {{filename1}}`

- Calculați sumele de verificare SHA224 pentru mai multe fișiere:

`sha224sum {{filename1}} {{filename2}}`

- Calculați și salvați lista sumelor de verificare SHA224 într-un fișier:

`sha224sum {{filename1}} {{filename2}} > {{filename.sha224}}`

- Citiți un fișier de sume SHA224 și verificați toate fișierele au sume de control potrivite:

`sha224sum --check {{filename.sha224}}`

- Afișați doar un mesaj pentru fișierele pentru care verificarea nu reușește:

`sha224sum --check --quiet {{filename.sha224}}`
