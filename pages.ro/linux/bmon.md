# bmon

> Monitorizează lățimea de bandă și captează statistici legate de rețea.
> Mai multe informaţii: <https://github.com/tgraf/bmon>

- Afișează lista tuturor interfețelor:

`bmon -a`

- Afișează ratele de transfer de date în biți pe secundă:

`bmon -b`

- Setați politica pentru a defini ce interfață (interfețe) de rețea este/sunt afișate:

`bmon -p {{interface_1,interface_2,interface_3}}`

- Setați intervalul (în secunde) în care se calculează rata pe contor:

`bmon -R {{2.0}}`
