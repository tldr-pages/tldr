# repquota

> Afișați un rezumat al cotelor de fișiere existente pentru un sistem de fișiere.

- Raportați statistici pentru toate contingentele utilizate:

`sudo repquota -all`

- Raportați statistici de cotă pentru toți utilizatorii, chiar și pentru cei care nu folosesc niciuna din cotele lor:

`sudo repquota -v {{filesystem}}`

- Raport privind cotele doar pentru utilizatori:

`repquota --user {{filesystem}}`

- Raport privind contingentele numai pentru grupuri:

`sudo repquota --group {{filesystem}}`

- Raport privind cota și limitele utilizate într-un format care poate fi citit de către om:

`sudo repquota --human-readable {{filesystem}}`

- Raport privind toate cotele pentru utilizatori și grupuri într-un format care poate fi citit de către om:

`sudo repquota -augs`
