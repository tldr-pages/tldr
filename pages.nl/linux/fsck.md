# fsck

> Controleer de integriteit van een bestandssysteem of repareer het. Het bestandssysteem moet niet gemount zijn op het moment dat het commando wordt uitgevoerd.
> Meer informatie: <https://manned.org/fsck>.

- Controleer bestandssysteem `/dev/sdXN` en rapporteer beschadigde blokken:

`sudo fsck {{/dev/sdXN}}`

- Controleer bestandssysteem `/dev/sdXN`, rapporteer beschadigde blokken en laat de gebruiker interactief kiezen om elke blok te repareren:

`sudo fsck -r {{/dev/sdXN}}`

- Controleer bestandssysteem `/dev/sdXN`, rapporteer beschadigde blokken en repareer ze automatisch:

`sudo fsck -a {{/dev/sdXN}}`
