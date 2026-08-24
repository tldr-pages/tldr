# ssh

> Secure Shell is een protocol waarmee op een veilige manier ingelogd kan worden op externe systemen.
> Het kan gebruikt worden voor het loggen of uitvoeren van opdrachten op een externe server.
> Meer informatie: <https://man.openbsd.org/ssh>.

- Verbind met een externe server:

`ssh {{gebruikersnaam}}@{{externe_host}}`

- Verbind met een externe server met een specifieke identiteit (privésleutel):

`ssh {{gebruikersnaam}}@{{externe_host}} -i {{pad/naar/sleutel_bestand}}`

- Verbind met een externe server met IP `10.0.0.1` en gebruik een specifieke [p]oort (Opmerking: `10.0.0.1` kan worden afgekort tot `10.1`):

`ssh {{gebruikersnaam}}@10.0.0.1 -p {{2222}}`

- Voer een opdracht uit op een externe server met een [t]ty-toewijzing die interactie met de externe opdracht toestaat:

`ssh {{gebruikersnaam}}@{{externe_host}} -t {{opdracht}} {{opdrachtargumenten}}`

- SSH-tunneling: [D]ynamische poortdoorsturing (SOCKS-proxy op `localhost:1080`):

`ssh {{gebruikersnaam}}@{{externe_host}} -D {{1080}}`

- SSH-tunneling: Stuur een specifieke poort door (`localhost:9999` naar `voorbeeld.org:80`) en schakel pseudo-[T]ty toewijzing en uitvoeri[N]g van externe opdrachten uit:

`ssh {{gebruikersnaam}}@{{externe_host}} -L {{9999}}:{{voorbeeld.org}}:{{80}} -N -T`

- SSH [J]umping: Verbind door een jumphost met een externe server (Meerdere jump hops mogen gespecificeerd worden door te splitsen met komma's):

`ssh {{gebruikersnaam}}@{{externe_host}} -J {{gebruikersnaam}}@{{jump_host}}`

- Sluit een vastgelopen sessie:

`<Enter><~><.>`
