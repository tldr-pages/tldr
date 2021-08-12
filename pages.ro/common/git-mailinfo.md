# git mailinfo

> Extrageţi informaţiile despre corecţii şi autori dintr-un singur mesaj de poştă electronică.
> Mai multe informaţii: <https://git-scm.com/docs/git-mailinfo>

- Extrageți datele patch-ului și ale autorului dintr-un mesaj de e-mail:

`git mailinfo {{message|patch}}`

- Extrageţi, dar eliminaţi spaţiul alb de conducere şi la final:

`git mailinfo -k {{message|patch}}`

- Scoateți totul din corp înainte de o linie de foarfece (de exemplu, „—>* —”) și preluați mesajul sau patch-ul:

`git mailinfo --scissors {{message|patch}}`
