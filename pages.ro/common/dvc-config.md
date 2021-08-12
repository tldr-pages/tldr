# dvc config

> Comandă de nivel scăzut pentru gestionarea opțiunilor de configurare particularizate pentru depozitele dvc.
> Aceste configurații pot fi la nivel de proiect, local, global sau sistem.
> Mai multe informaţii: <https://dvc.org/doc/command-reference/config>

- Obțineți numele telecomenzii implicite:

`dvc config core.remote`

- Setați telecomanda implicită a proiectului:

`dvc config core.remote {{remote_name}}`

- Anulează telecomanda implicită a proiectului:

`dvc config --unset core.remote`

- Obțineți valoarea de configurare pentru o cheie specificată pentru proiectul curent:

`dvc config {{key}}`

- Setați valoarea de configurare pentru o cheie la nivel de proiect:

`dvc config {{key}} {{value}}`

- Anulați o valoare de configurare la nivel de proiect pentru o cheie dată:

`dvc config --unset {{key}}`

- Setați o valoare de configurare locală, globală sau la nivel de sistem:

`dvc config --local/global/system {{key}} {{value}}`
