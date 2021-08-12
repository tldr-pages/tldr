# hub

> Un înveliș pentru Git care adaugă comenzi pentru lucrul cu proiecte bazate pe Githubb.
> Dacă este configurat conform instrucțiunilor de `hub alias', se poate folosi `git` pentru a rula comenzi `hub`.
> Mai multe informaţii: <https://hub.github.com>

- Clonează un depozit folosind melcul său (proprietarii pot omite numele de utilizator):

`hub clone {{username}}/{{repo_name}}`

- Creați o furculiță a depozitului curent (clonat de la un alt utilizator) sub profilul dvs. GitHub:

`hub fork`

- Împingeți sucursala locală curentă la GitHub și creați un PR pentru aceasta în depozitul original:

`hub push {{remote_name}} && hub pull-request`

- Creați un PR al ramurii curente (deja împinse), reutilizând mesajul de la primul angajament:

`hub pull-request --no-edit`

- Creați o nouă ramură cu conținutul unei cereri de tragere și treceți la ea:

`hub pr checkout {{pr_number}}`

- Încărcați depozitul curent (doar local) în contul dvs. GitHub:

`hub create`

- Adu obiecte Git din amonte și actualizează sucursalele locale:

`hub sync`
