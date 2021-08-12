# shasum

> Calculați sau verificați sumele de control SHA criptografice.

- Calculați suma de control SHA1 pentru un fișier:

`shasum {{filename}}`

- Calculați suma de control SHA256 pentru un fișier:

`shasum --algorithm 256 {{filename}}`

- Calculați suma de control SHA512 pentru mai multe fișiere:

`shasum --algorithm 512 {{filename1}} {{filename2}}`

- Calculați și salvați lista sumelor de control SHA256 într-un fișier:

`shasum --algorithm 256 {{filename1}} {{filename2}} > {{filename.sha256}}`

- Verificați un fișier cu o listă de sume împotriva fișierelor directorului:

`shasum --check {{list_file}}`

- Verificați o listă de sume și afișați doar un mesaj pentru fișierele pentru care verificarea nu reușește:

`shasum --check --quiet {{list_file}}`

- Calculați suma de control SHA1 din stdin:

`{{somecommand}} | shasum`
