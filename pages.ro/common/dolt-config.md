# dolt config

> Citiți și scrieți locale (per depozit) și globale (per utilizator) variabile de configurare Dolt.
> Mai multe informaţii: <https://docs.dolthub.com/interfaces/cli#dolt-config>

- Listează toate opțiunile de configurare locale și globale și valorile acestora:

`dolt config --list`

- Afișează valoarea unei variabile de configurare locală sau globală:

`dolt config --get {{name}}`

- Modificați valoarea unei variabile de configurare locală, creând-o dacă nu există:

`dolt config --add {{name}} {{value}}`

- Modificați valoarea unei variabile de configurare globală, creând-o dacă nu există:

`dolt config --global --add {{name}} {{value}}`

- Ștergeți o variabilă de configurare locală:

`dolt config --unset {{name}}`

- Ștergeți o variabilă de configurare globală:

`dolt config --global --unset {{name}}`
