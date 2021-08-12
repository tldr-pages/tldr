# ping

> Trimiteți pachete ICMP ECHO_REQUEST către gazdele de rețea.

- Gazda Ping:

`ping {{host}}`

- Ping o gazdă doar un anumit număr de ori:

`ping -c {{count}} {{host}}`

- Ping gazdă, specificând intervalul în secunde între cereri (implicit este 1 secundă):

`ping -i {{seconds}} {{host}}`

- Ping gazdă fără a încerca să caute nume simbolice pentru adrese:

`ping -n {{host}}`

- Ping gazdă și sunați clopotul atunci când un pachet este primit (dacă terminalul dvs. îl acceptă):

`ping -a {{host}}`

- De asemenea, afișați un mesaj dacă nu a fost primit niciun răspuns:

`ping -O {{host}}`
