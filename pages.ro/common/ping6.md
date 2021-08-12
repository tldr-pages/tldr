# ping6

> Trimiteți pachete ICMP ECHO_REQUEST către gazdele de rețea prin adresa IPv6.

- Ping o gazdă:

`ping6 {{host}}`

- Ping o gazdă doar un anumit număr de ori:

`ping6 -c {{count}} {{host}}`

- Ping o gazdă, specificând intervalul în secunde între solicitări (implicit este 1 secundă):

`ping6 -i {{seconds}} {{host}}`

- Ping o gazdă fără a încerca să caute nume simbolice pentru adrese:

`ping6 -n {{host}}`

- Ping o gazdă și sunați clopotul atunci când un pachet este primit (dacă terminalul dvs. îl acceptă):

`ping6 -a {{host}}`
