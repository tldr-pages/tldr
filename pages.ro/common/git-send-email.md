# git send-email

> Trimiteți o colecție de patch-uri ca e-mailuri.
> Corecțiile pot fi specificate ca fișiere, indicații de orientare sau o listă de revizii.
> Mai multe informaţii: <https://git-scm.com/docs/git-send-email>

- Trimite ultimul angajament în sucursala curentă:

`git send-email -1`

- Trimite un angajament dat:

`git send-email -1 {{commit}}`

- Trimite mai multe (ex. 10) angajamente în sucursala curentă:

`git send-email {{-10}}`

- Trimiteți un mesaj de e-mail introductiv pentru seria de patch-uri:

`git send-email -{{number_of_commits}} --compose`

- Revizuiți și editați mesajul de e-mail pentru fiecare patch pe care urmează să îl trimiteți:

`git send-email -{{number_of_commits}} --annotate`
