# nc

> Netcat is een veelzijdig hulpprogramma voor het omleiden van IO naar een netwerkstream.
> Meer informatie: <https://manned.org/man/nc.1>.

- Start een luisteraar op de opgegeven TCP poort en stuur er een bestand in:

`nc -l -p {{poort}} < {{bestandsnaam}}`

- Maak verbinding met een doelluisteraar op de opgegeven poort en ontvang er een bestand uit:

`nc {{host}} {{poort}} > {{ontvangen_bestandsnaam}}`

- Scan de open TCP poorten van een opgegeven host:

`nc -v -z -w {{timeout_in_seconden}} {{host}} {{start_port}}-{{end_port}}`

- Start een luisteraar op de opgegeven TCP poort en geef uw lokale shell toegang tot de verbonden partij (dit is gevaarlijk en kan worden misbruikt):

`nc -l -p {{poort}} -e {{shell_executable}}`

- Maak verbinding met een doelluisteraar en geef uw lokale shell toegang tot de externe partij (dit is gevaarlijk en kan worden misbruikt):

`nc {{host}} {{poort}} -e {{shell_executable}}`

- Fungeer als een proxy en stuur gegevens door van een lokale TCP poort naar de opgegeven externe host:

`nc -l -p {{local_port}} | nc {{host}} {{remote_port}}`

- Stuur een HTTP GET verzoek:

`echo -e "GET / HTTP/1.1\nHost: {{host}}\n\n" | nc {{host}} 80`
