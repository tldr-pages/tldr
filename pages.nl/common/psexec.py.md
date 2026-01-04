# psexec.py

> Voer commando's uit op een Windows machine op afstand met `RemComSvc`, met PsExec-achtige functionaliteit.
> Part of the Impacket suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Start een interactieve shell op een extern doelwit:

`psexec.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Voer een specifiek commando uit op een doel op afstand:

`psexec.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}} {{commando}}`

- Kopieer de bestandsnaam voor latere uitvoering, argumenten worden doorgegeven in het commando:

`psexec.py -c {{bestandsnaam}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}} {{commando}}`

- Voer een commando uit vanaf een specifiek pad op een extern doelwit:

`psexec.py -path {{path}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}} {{commando}}`

- Authenticeer met pass-the-hash-authenticatie in plaats van een wachtwoord:

`psexec.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Gebruik Kerberos verificatie voor het doel:

`psexec.py -k -no-pass {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Specificeer het IP-adres van de domeincontroller:

`psexec.py -dc-ip {{domain_controller_ip}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`
