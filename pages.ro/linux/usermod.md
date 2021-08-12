# usermod

> Modifică un cont de utilizator.
> Mai multe informaţii: <https://manned.org/usermod>

- Schimbarea numelui unui utilizator:

`usermod -l {{newname}} {{user}}`

- Adaugă utilizator la grupuri suplimentare (minte spațiul alb):

`usermod -a -G {{group1,group2}} {{user}}`

- Creați un nou director de acasă pentru un utilizator și mutați fișierele lor la el:

`usermod -m -d {{path/to/home}} {{user}}`
