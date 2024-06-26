# xargs

> Voer een commando uit met doorgegeven argumenten van een ander commando, een bestand, etc.
> De invoer wordt behandeld als een enkel tekstblok en gesplitst in afzonderlijke stukken op spaties, tabbladen, nieuwe regels en einde-van-bestand.
> Meer informatie: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html>.

- Voer een commando uit met de invoergegevens als argumenten:

`{{argumenten_bron}} | xargs {{commando}}`

- Voer meerdere gekoppelde commando's uit op de invoergegevens:

`{{argumenten_bron}} | xargs sh -c "{{commando1}} && {{commando2}} | {{commando3}}"`

- Verwijder alle bestanden met een `.backup` extensie (`-print0` gebruikt een nul-teken om bestandsnamen te splitsen en `-0` gebruikt het als scheidingsteken):

`find . -name '*.backup' -print0 | xargs -0 rm -v`

- Voer het commando één keer uit voor elke invoerregel, waarbij elke plaatsaanduiding (hier gemarkeerd als `_`) wordt vervangen door de invoerregel:

`{{argumenten_bron}} | xargs -I _ {{commando}} _ {{optionele_extra_argumenten}}`

- Parallelle uitvoeringen van maximaal `max-procs` processen tegelijk; de standaard is 1. Als `max-procs` 0 is, zal xargs zoveel mogelijk processen tegelijk uitvoeren:

`{{argumenten_bron}} | xargs -P {{max-procs}} {{commando}}`
