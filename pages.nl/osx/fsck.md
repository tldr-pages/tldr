# fsck

> Controleer de integriteit van een bestandssysteem of repareer het. Het bestandssysteem moet niet gemount zijn op het moment dat het commando wordt uitgevoerd.
> Het is een wrapper die `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat` en `fsck_udf` aanroept indien nodig.
> Meer informatie: <https://keith.github.io/xcode-man-pages/fsck.8.html>.

- Controleer bestandssysteem `/dev/sdX` en rapporteer beschadigde blokken:

`fsck {{/dev/sdX}}`

- Controleer bestandssysteem `/dev/sdX` alleen als het schoon is, rapporteer beschadigde blokken en laat de gebruiker interactief kiezen om elke blok te repareren:

`fsck -f {{/dev/sdX}}`

- Controleer bestandssysteem `/dev/sdX` alleen als het schoon is, rapporteer beschadigde blokken en repareer ze automatisch:

`fsck -fy {{/dev/sdX}}`

- Controleer bestandssysteem `/dev/sdX` en rapporteer of het schoon is afgekoppeld:

`fsck -q {{/dev/sdX}}`
