# Stormlock

> Sistem centralizat de blocare.
> Mai multe informaţii: <https://github.com/tmccombs/stormlock>

- Achiziționați un contract de închiriere pentru resurse:

`stormlock aquire {{resource}}`

- Eliberați contractul de închiriere dat pentru resursa dată:

`stormlock release {{resource}} {{lease_id}}`

- Afișați informații despre contractul de închiriere curent pentru o resursă, dacă există:

`stormlock current {{resource}}`

- Testați dacă un contract de închiriere pentru resursă dată este activ în prezent:

`stormlock is-held {{resource}} {{lease_id}}`
