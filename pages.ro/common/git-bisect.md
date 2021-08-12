# git bisect

> Utilizați căutarea binară pentru a găsi comiterea care a introdus o eroare.
> Git sare automat înainte și înapoi în graficul de angajare pentru a restrânge progresiv comiterea defectuoasă.
> Mai multe informaţii: <https://git-scm.com/docs/git-bisect>

- Începeți o sesiune de bisect pe un interval de comitere delimitat de un buggy cunoscut și un cunoscut curat (de obicei mai vechi):

`git bisect start {{bad_commit}} {{good_commit}}`

- Pentru fiecare comitet selectat `git bisect`, marcați-l ca „rău” sau „bun” după testarea emisiunii:

`git bisect {{good|bad}}`

- După ce `git bisect` identifică comiterea defectuoasă, încheie sesiunea de bisect și reveniți la ramura anterioară:

`git bisect reset`

- Săriți o comitere în timpul unui bisect (de exemplu, una care nu reușește testele din cauza unei probleme diferite):

`git bisect skip`
