# sha256sum

> Calculați sumele de verificare criptografice SHA256.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>

- Calculați suma de control SHA256 pentru un fișier:

`sha256sum {{filename1}}`

- Calculați sumele de control SHA256 pentru mai multe fișiere:

`sha256sum {{filename1}} {{filename2}}`

- Calculați și salvați lista sumelor de control SHA256 într-un fișier:

`sha256sum {{filename1}} {{filename2}} > {{filename.sha256}}`

- Citiți un fișier de sume SHA256 și verificați toate fișierele au sume de control potrivite:

`sha256sum --check {{filename.sha256}}`

- Afișați doar un mesaj pentru fișierele pentru care verificarea nu reușește:

`sha256sum --check --quiet {{filename.sha256}}`
