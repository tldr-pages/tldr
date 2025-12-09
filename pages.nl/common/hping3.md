# hping3

> Geavanceerd pinghulpprogramma dat protocollen ondersteunt zoals TCP, UDP en IP.
> Dit kan het beste uitgevoerd worden met extra priveleges.
> Meer informatie: <https://manned.org/hping3>.

- Ping een bestemming met 4 ICMP ping aanvragen:

`hping3 {{[-1|--icmp]}} {{[-c|--count]}} 4 {{ip_of_hostnaam}}`

- Ping een IP addres over UDP op poort 80:

`hping3 {{[-2|--udp]}} {{[-p|--destport]}} 80 {{[-S|--syn]}} {{ip_of_hostnaam}}`

- Scan TCP poort 80, maar scan vanaf de specifieke lokale bronpoort 5090:

`hping3 {{[-V|--verbose]}} {{[-S|--syn]}} {{[-p|--destport]}} 80 {{[-s|--baseport]}} 5090 {{ip_of_hostnaam}}`

- Traceroute met behulp van een TCP scan naar een specifieke bestemmingspoort:

`hping3 {{[-T|--traceroute]}} {{[-V|--verbose]}} {{[-S|--syn]}} {{[-p|--destport]}} {{80}} {{ip_of_hostnaam}}`

- Scan een set van TCP poorten op een specifiek IP adres:

`hping3 {{[-8|--scan]}} {{80,3000,9000}} {{[-S|--syn]}} {{ip_of_hostnaam}}`

- Voer een TCP ACK scan uit om te checken of een gegeven host nog leeft:

`hping3 {{[-c|--count]}} {{2}} {{[-V|--verbose]}} {{[-p|--destport]}} {{80}} {{[-A|--ack]}} {{ip_of_hostnaam}}`

- Voer een charge test uit op poort 80:

`hping3 --flood {{[-p|--destport]}} 80 {{[-S|--syn]}} {{ip_of_hostnaam}}`
