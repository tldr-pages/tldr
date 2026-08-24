# xargs

> Voer een commando uit met doorgegeven argumenten van een ander commando, een bestand, etc.
> De invoer wordt behandeld als een enkel tekstblok en gesplitst in afzonderlijke stukken op spaties, tabbladen, nieuwe regels en einde-van-bestand.
> Zie ook: `parallel`.
> Meer informatie: <https://www.gnu.org/software/findutils/manual/html_mono/find.html#Invoking-xargs>.

- Voer een commando uit met de invoergegevens als argumenten:

`{{argumenten_bron}} | xargs {{commando}}`

- Voer meerdere gekoppelde commando's uit op de invoergegevens:

`{{argumenten_bron}} | xargs sh -c "{{commando1}} && {{commando2}} | {{commando3}}"`

- Voer een nieuwe commando uit met elk argument:

`{{argumenten_bron}} | xargs {{[-n|--max-args]}} 1 {{commando}}`

- Verhoog het limiet voor parallelle processen naar 10 (standaard is 1; 0 betekent zoveel mogelijk processen):

`{{argumenten_bron}} | xargs {{[-P|--max-procs]}} 10 {{[-n|--max-args]}} {{1}} {{commando}}`

- Voer het commando één keer uit voor elke invoerregel, waarbij elke plaatsaanduiding (hier gemarkeerd als `_`) wordt vervangen door de invoerregel:

`{{argumenten_bron}} | xargs -I _ {{commando}} _ {{optionele_extra_argumenten}}`

- Vraag de gebruiker om bevestiging voordat de opdracht wordt uitgevoerd (bevestig met `y` of `Y`):

`{{argumenten_bron}} | xargs {{[-p|--interactive]}} {{commando}}`

- Lees een bestand voor argumenten die worden doorgegeven aan een commando:

`xargs {{[-a|--arg-file]}} {{pad/naar/bestand}} {{commando}}`

- Geef het commando toegang tot de terminal voor interactieve invoer:

`{{argumenten_bron}} | xargs {{[-o|--open-tty]}} {{commando}}`
