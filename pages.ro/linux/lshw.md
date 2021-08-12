# lshw

> Listați informații detaliate despre configurațiile hardware ca utilizator rădăcină.

- Lansarea GUI:

`sudo lshw -X`

- Listează toate hardware-ul în format tabelar:

`sudo lshw -short`

- Listați toate discurile și controlerele de stocare în format tabelar:

`sudo lshw -class disk -class storage -short`

- Salvați toate interfețele de rețea într-un fișier HTML:

`sudo lshw -class network -html > {{interfaces.html}}`
