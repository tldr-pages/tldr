# eject

> Éjecte les CD, disquettes et les bandes magnétiques.
> Plus d'informations : <https://manned.org/eject>.

- Affiche l'appareil par défaut :

`eject -d`

- Éjecte l'appareil par défaut :

`eject`

- Éjecte un appareil spécifique (l'ordre par défaut est CD-ROM, SCSI, Disquette puis bande magnétique) :

`eject {{/dev/cdrom}}`

- Bascule le support d'appareil en mode ouvert ou fermé :

`eject -T {{/dev/cdrom}}`

- Éjecte un CD :

`eject -r {{/dev/cdrom}}`

- Éjecte une disquette :

`eject -f {{/mnt/disquette}}`

- Éjecte une bande magnétique :

`eject -q {{/mnt/bande}}`
