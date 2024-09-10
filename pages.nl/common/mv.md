# mv

> Verplaats of hernoem bestanden en mappen.
> Meer informatie: <https://www.gnu.org/software/coreutils/mv>.

- Hernoem een bestand of map als het doel geen bestaande map is:

`mv {{pad/naar/bron}} {{pad/naar/doel}}`

- Verplaats een bestand of map naar een bestaande map:

`mv {{pad/naar/bron}} {{pad/naar/bestaande_map}}`

- Verplaats meerdere bestanden naar een bestaande map, waarbij de bestandsnamen ongewijzigd blijven:

`mv {{pad/naar/bron1 pad/naar/bron2 ...}} {{pad/naar/bestaande_map}}`

- Vraag niet om bevestiging ([f]) voordat bestaande bestanden worden overschreven:

`mv --force {{pad/naar/bron}} {{pad/naar/doel}}`

- Vraag om bevestiging [i]nteractief voordat bestaande bestanden worden overschreven, ongeacht de bestandsrechten:

`mv --interactive {{pad/naar/bron}} {{pad/naar/doel}}`

- Overschrijf ([n]) geen bestaande bestanden op de doelbestemming:

`mv --no-clobber {{pad/naar/bron}} {{pad/naar/doel}}`

- Verplaats bestanden in [v]erbose-modus, waarbij de bestanden worden getoond nadat ze zijn verplaatst:

`mv --verbose {{pad/naar/bron}} {{pad/naar/doel}}`

- Specificeer de doelmap ([t]) (handig in situaties waarin de doelmap het eerste argument moet zijn):

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv --target-directory {{pad/naar/doel_map}}`
