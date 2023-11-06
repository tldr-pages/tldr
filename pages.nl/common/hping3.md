# hping3

> Geavanceerd pinghulpprogramma dat protocollen ondersteunt zoals TCP, UDP en IP.
> Dit kan het beste uitgevoerd worden met extra priveleges.
> Meer informatie: <https://github.com/antirez/hping>.

- Ping een bestemming met 4 ICMP ping aanvragen:

`hping3 --icmp --count {{4}} {{ip_of_hostnaam}}`

- Ping een IP addres over UDP op poort 80:

`hping3 --udp --destport {{80}} --syn {{ip_of_hostnaam}}`

- Scan TCP poort 80, maar scan vanaf de specifieke lokale bronpoort 5090:

`hping3 --verbose --syn --destport {{80}} --baseport {{5090}} {{ip_of_hostnaam}}`

- Traceroute met behulp van een TCP scan naar een specifieke bestemmingspoort:

`hping3 --traceroute --verbose --syn --destport {{80}} {{ip_of_hostnaam}}`

- Scan een set van TCP poorten op een specifiek IP adres:

`hping3 --scan {{80,3000,9000}} --syn {{ip_of_hostnaam}}`

- Voer een TCP ACK scan uit om te checken of een gegeven host nog leeft:

`hping3 --count {{2}} --verbose --destport {{80}} --ack {{ip_of_hostnaam}}`

- Voer een charge test uit op poort 80:

`hping3 --flood --destport {{80}} --syn {{ip_of_hostnaam}}`
