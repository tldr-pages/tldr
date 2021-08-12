# sha1sum

> Calculați sumele de verificare criptografice SHA1.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/sha1sum>

- Calculați suma de control SHA1 pentru un fișier:

`sha1sum {{filename1}}`

- Calculați sumele de control SHA1 pentru mai multe fișiere:

`sha1sum {{filename1}} {{filename2}}`

- Calculați și salvați lista sumelor de verificare SHA1 într-un fișier:

`sha1sum {{filename1}} {{filename2}} > {{filename.sha1}}`

- Citiți un fișier de sume SHA1 și verificați toate fișierele au sume de control potrivite:

`sha1sum --check {{filename.sha1}}`

- Afișați doar un mesaj pentru fișierele pentru care verificarea nu reușește:

`sha1sum --check --quiet {{filename.sha1}}`
