# infection

> Un cadru de testare a mutațiilor pentru PHP.
> Mai multe informaţii: <https://infection.github.io>

- Analizați codul utilizând fișierul de configurare (sau creați unul dacă nu există):

`infection`

- Utilizați un anumit număr de fire:

`infection --threads {{number_of_threads}}`

- Specificaţi indicatorul punctajului minim de mutaţie (MSI):

`infection --min-msi {{percentage}}`

- A se specifica un cod minim acoperit MSI:

`infection --min-covered-msi {{percentage}}`

- Utilizați un cadru de testare specific (implicit la phpunit):

`infection --test-framework {{phpunit|phpspec}}`

- Numai liniile de cod mutante care sunt acoperite de teste:

`infection --only-covered`

- Afișează codul de mutație care a fost aplicat:

`infection --show-mutations`

- Specificați verbozitatea jurnalului:

`infection --log-verbosity {{default|all|none}}`
