# semanage

> SELinux persistent beleid beheertool.
> Sommige subcommando's zoals `boolean`, `fcontext`, `port`, etc. hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://manned.org/semanage>.

- Stel een SELinux-boolean in of uit. Booleans stellen de beheerder in staat om aan te passen hoe beleidsregels invloed hebben op ingesloten procestypes (ook wel domeinen genoemd):

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`

- Voeg een door de gebruiker gedefinieerde bestandscontextlabelregel toe. Bestandscontexten definiëren welke bestanden ingesloten domeinen mogen openen:

`sudo semanage fcontext {{[-a|--add]}} {{[-t|--type]}} {{samba_share_t}} '/mnt/share(/.*)?'`

- Voeg een door de gebruiker gedefinieerde poortlabelregel toe. Poortlabels definiëren op welke poorten ingesloten domeinen mogen luisteren:

`sudo semanage port {{[-a|--add]}} {{[-t|--type]}} {{ssh_port_t}} {{[-p|--proto]}} {{tcp}} {{22000}}`

- Stel de permissieve modus in of uit voor een ingesloten domein. Per-domein permissieve modus biedt meer gedetailleerde controle vergeleken met `setenforce`:

`sudo semanage permissive {{-a|--add|-d|--delete}} {{httpd_t}}`

- Exporteer lokale aanpassingen in de standaardopslag:

`sudo semanage export {{[-f|--output_file]}} {{pad/naar/bestand}}`

- Importeer een bestand gegenereerd door `semanage export` in lokale aanpassingen (VOORZICHTIG: kan huidige aanpassingen verwijderen!):

`sudo semanage import {{[-f|--input_file]}} {{pad/naar/bestand}}`
