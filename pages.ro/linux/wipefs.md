# wipefs

> Ștergeți semnăturile sistemului de fișiere, raidului sau tabelului de partiții de pe un dispozitiv.

- Semnături de afișare pentru dispozitivul specificat:

`sudo wipefs {{/dev/sdX}}`

- Ștergeți toate semnăturile disponibile pentru dispozitivul specificat:

`sudo wipefs --all {{/dev/sdX}}`

- Efectuați o funcționare uscată:

`sudo wipefs --all --no-act {{/dev/sdX}}`

- Ștergeți forța, chiar dacă sistemul de fișiere este montat:

`sudo wipefs --all --force {{/dev/sdX}}`
