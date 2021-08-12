# ipcalc

> Efectuați operații și calcule simple pe adrese IP și rețele.

- Afișați informații despre o adresă sau o rețea cu o mască de subrețea dată:

`ipcalc {{1.2.3.4}} {{255.255.255.0}}`

- Afișați informații despre o adresă sau o rețea în notația CIDR:

`ipcalc {{1.2.3.4}}/{{24}}`

- Afișați adresa de difuzare a unei adrese sau a unei rețele:

`ipcalc -b {{1.2.3.4}}/{{30}}`

- Afișați adresa de rețea a adresei IP furnizate și netmask:

`ipcalc -n {{1.2.3.4}}/{{24}}`

- Afișează informații geografice despre o adresă IP dată:

`ipcalc -g {{1.2.3.4}}`
