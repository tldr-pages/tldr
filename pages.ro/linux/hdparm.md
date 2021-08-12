# hdparm

> Obțineți și setați parametrii hard diskului SATA și IDE.

- Solicitați informațiile de identificare ale unui anumit dispozitiv:

`sudo hdparm -I /dev/{{device}}`

- Obțineți nivelul Advanced Power Management:

`sudo hdparm -B /dev/{{device}}`

- Setați valoarea Advanced Power Management (valorile 1-127 permit spin-down, iar valorile 128-254 nu):

`sudo hdparm -B {{1}} /dev/{{device}}`

- Afișează starea modului curent de alimentare al dispozitivului:

`sudo hdparm -C /dev/{{device}}`

- Forțați o unitate să intre imediat în modul de așteptare (de obicei determină o unitate să se rotească în jos):

`sudo hdparm -y /dev/{{device}}`

- Puneți unitatea în modul inactiv (cu putere redusă), setând și timpul de expirare în așteptare:

`sudo hdparm -S {{standby_timeout}} {{device}}`
