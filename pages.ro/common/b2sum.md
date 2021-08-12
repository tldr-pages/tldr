# b2sum

> Calculați sumele de verificare criptografice BLAKE2.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/b2sum>

- Calculați suma de control BLAKE2 pentru un fișier:

`b2sum {{filename1}}`

- Calculați sumele de control BLAKE2 pentru mai multe fișiere:

`b2sum {{filename1}} {{filename2}}`

- Citiți un fișier de sume BLAKE2 și nume de fișiere și verificați toate fișierele au sume de control de potrivire:

`b2sum -c {{filename.b2}}`

- Calculați suma de control BLAKE2 din stdin:

`{{somecommand}} | b2sum`
