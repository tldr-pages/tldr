# iostat

> Raportați statistici pentru dispozitive și partiții.

- Afișează un raport de statistici CPU și disc de la pornirea sistemului:

`iostat`

- Afișați un raport de statistici CPU și disc cu unități convertite în megaocteți:

`iostat -m`

- Afișează statistici CPU:

`iostat -c`

- Afișează statistici de disc cu nume de disc (inclusiv LVM):

`iostat -N`

- Afișează statistici extinse de disc cu nume de disc pentru dispozitiv „sda”:

`iostat -xN {{sda}}`

- Afișează rapoarte incrementale ale statisticilor CPU și disc la fiecare 2 secunde:

`iostat {{2}}`
