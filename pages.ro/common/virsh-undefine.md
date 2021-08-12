# virsh-undefine

> Ștergeți o mașină virtuală.
> Mai multe informaţii: <https://manned.org/virsh>

- Ștergeți numai fișierul de configurare mașină virtuală:

`virsh undefine --domain {{vm_name}}`

- Ștergeți fișierul de configurare și toate volumele de stocare asociate:

`virsh undefine --domain {{vm_name}} --remove-all-storage`

- Ștergeți fișierul de configurare și volumele de stocare specificate utilizând numele țintă sau numele sursei (așa cum se obține din comanda `virsh domblklist`):

`virsh undefine --domain {{vm_name}} --storage {{sda,path/to/source}}`
