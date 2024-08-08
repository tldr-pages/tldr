# at

> Voer commando's eenmaal later uit.
> De service atd (of atrun) moet actief zijn voor de daadwerkelijke uitvoering.
> Meer informatie: <https://manned.org/at>.

- Voer commando's uit van `stdin` over 5 minuten (druk op `Ctrl + D` als je klaar bent):

`at now + 5 minutes`

- Voer een commando uit van `stdin` om 10:00 AM vandaag:

`echo "{{./make_db_backup.sh}}" | at 1000`

- Voer commando's uit van een gegeven bestand volgende dinsdag:

`at -f {{pad/naar/bestand}} 9:30 PM Tue`
